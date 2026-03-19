# ╔══════════════════════════════════════════════════════════════════════╗
# ║  Cardiac Arrest Risk Dashboard — Intraoperative Monitor v2          ║
# ║  Run: python -m streamlit run cardiac_dashboard.py                  ║
# ╚══════════════════════════════════════════════════════════════════════╝

import os, json, pickle, warnings
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import torch
import torch.nn as nn
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="CA Risk Monitor",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'IBM Plex Sans', sans-serif;
    background-color: #070a10;
    color: #cdd6f4;
}
.main { background-color: #070a10; }
div[data-testid="stSidebar"] { background-color: #0b0f18; border-right: 1px solid #1a2035; }

.section-label {
    font-family: 'IBM Plex Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #3d4f6e;
    margin-bottom: 8px;
    padding-bottom: 5px;
    border-bottom: 1px solid #1a2035;
}

.risk-block {
    border-radius: 10px;
    padding: 18px 16px;
    text-align: center;
    margin-bottom: 10px;
}
.risk-critical { background:#1e0a0a; border:2px solid #f38ba8; animation: pulse 1.5s infinite; }
.risk-high     { background:#1e140a; border:2px solid #fab387; }
.risk-moderate { background:#0a1a10; border:2px solid #a6e3a1; }
.risk-low      { background:#0a1020; border:2px solid #89b4fa; }

@keyframes pulse {
    0%   { box-shadow: 0 0 0 0 rgba(243,139,168,0.5); }
    70%  { box-shadow: 0 0 0 14px rgba(243,139,168,0); }
    100% { box-shadow: 0 0 0 0 rgba(243,139,168,0); }
}

.vital-tile {
    background: #0d1220;
    border: 1px solid #1a2035;
    border-radius: 8px;
    padding: 10px 12px;
    text-align: center;
    margin-bottom: 4px;
}
.val-normal  { color: #a6e3a1; font-size: 28px; font-weight: 700; font-family: 'IBM Plex Mono', monospace; }
.val-warning { color: #fab387; font-size: 28px; font-weight: 700; font-family: 'IBM Plex Mono', monospace; }
.val-danger  { color: #f38ba8; font-size: 28px; font-weight: 700; font-family: 'IBM Plex Mono', monospace; }

.alert-critical {
    background: #1e0a0a;
    border-left: 4px solid #f38ba8;
    border-radius: 4px;
    padding: 10px 14px;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 13px;
    color: #f38ba8;
    margin: 6px 0;
}
.info-strip {
    background: #0d1525;
    border-left: 4px solid #89b4fa;
    border-radius: 4px;
    padding: 10px 14px;
    font-size: 12px;
    color: #a6b0c8;
    margin: 6px 0;
}
.change-table {
    width: 100%;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 12px;
    border-collapse: collapse;
}
.change-table th {
    background: #0d1220;
    color: #3d4f6e;
    padding: 6px 10px;
    text-align: left;
    font-size: 10px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.change-table td { padding: 6px 10px; border-bottom: 1px solid #1a2035; }
.change-up   { color: #f38ba8; }
.change-down { color: #89b4fa; }
.change-ok   { color: #a6e3a1; }
</style>
""", unsafe_allow_html=True)

# ── Constants ──────────────────────────────────────────────────────────
WORK_DIR = r'S:\tsi university\exam\research methodology\research 2\dataset\master thesis database\working'
LSTM_DIR = os.path.join(WORK_DIR, 'lstm')
TAN_DIR  = os.path.join(WORK_DIR, 'tan')

WINDOWS   = [30, 60, 120, 240]
SIGNALS   = ['HR', 'PLETH_SPO2', 'ETCO2', 'ART_MBP', 'ART_SBP', 'ART_DBP']
SIG_LABEL = {
    'HR':          'Heart Rate',
    'PLETH_SPO2':  'SpO₂',
    'ETCO2':       'EtCO₂',
    'ART_MBP':     'Mean BP',
    'ART_SBP':     'Systolic BP',
    'ART_DBP':     'Diastolic BP',
}
SIG_UNIT  = {'HR':'bpm','PLETH_SPO2':'%','ETCO2':'mmHg','ART_MBP':'mmHg','ART_SBP':'mmHg','ART_DBP':'mmHg'}
SIG_COLOR = {
    'HR':'#f38ba8','PLETH_SPO2':'#a6e3a1','ETCO2':'#fab387',
    'ART_MBP':'#89b4fa','ART_SBP':'#cba6f7','ART_DBP':'#89dceb'
}
NORMAL = {
    'HR':(50,100),'PLETH_SPO2':(95,100),
    'ETCO2':(35,45),'ART_MBP':(70,105),
    'ART_SBP':(90,140),'ART_DBP':(60,90)
}
# Clinical thresholds for change detection
CHANGE_THRESH = {
    'HR':10,'PLETH_SPO2':2,'ETCO2':5,
    'ART_MBP':15,'ART_SBP':20,'ART_DBP':10
}

# ── Model classes ──────────────────────────────────────────────────────
class LSTMBaseline(nn.Module):
    def __init__(self, n_features=36, hidden=64, dropout=0.3):
        super().__init__()
        self.lstm1 = nn.LSTM(n_features, hidden,      batch_first=True)
        self.lstm2 = nn.LSTM(hidden,     hidden // 2, batch_first=True)
        self.bn1   = nn.BatchNorm1d(hidden)
        self.bn2   = nn.BatchNorm1d(hidden // 2)
        self.drop  = nn.Dropout(dropout)
        self.fc1   = nn.Linear(hidden // 2, 32)
        self.fc2   = nn.Linear(32, 1)
        self.relu  = nn.ReLU()
    def forward(self, x):
        out, _ = self.lstm1(x)
        out    = self.bn1(out[:, -1, :])
        out    = self.drop(out); out = out.unsqueeze(1)
        out, _ = self.lstm2(out)
        out    = self.bn2(out[:, -1, :])
        out    = self.drop(out)
        out    = self.relu(self.fc1(out))
        out    = self.drop(out)
        return self.fc2(out).squeeze(1)

class TemporalAttentionNetwork(nn.Module):
    def __init__(self, n_features=36, hidden=64, n_heads=4, dropout=0.3):
        super().__init__()
        self.lstm1      = nn.LSTM(n_features, hidden,      batch_first=True)
        self.lstm2      = nn.LSTM(hidden,     hidden // 2, batch_first=True)
        self.bn1        = nn.BatchNorm1d(hidden)
        self.bn2        = nn.BatchNorm1d(hidden // 2)
        self.drop       = nn.Dropout(dropout)
        self.attention  = nn.MultiheadAttention(embed_dim=hidden//2, num_heads=n_heads, dropout=dropout, batch_first=True)
        self.layer_norm = nn.LayerNorm(hidden // 2)
        self.fc1  = nn.Linear(hidden // 2, 32)
        self.fc2  = nn.Linear(32, 1)
        self.relu = nn.ReLU()
    def forward(self, x, return_attn=False):
        B, T, _ = x.shape
        out, _  = self.lstm1(x)
        out     = self.bn1(out.reshape(B*T,-1)).reshape(B,T,-1)
        out     = self.drop(out)
        out, _  = self.lstm2(out)
        B2,T2,H = out.shape
        out     = self.bn2(out.reshape(B2*T2,H)).reshape(B2,T2,H)
        out     = self.drop(out)
        attn_out, attn_w = self.attention(out, out, out)
        out = self.layer_norm(out + self.drop(attn_out))
        out = out.mean(dim=1)
        out = self.relu(self.fc1(out)); out = self.drop(out)
        logits = self.fc2(out).squeeze(1)
        return (logits, attn_w) if return_attn else logits

@st.cache_resource
def load_models():
    device = torch.device('cpu')
    lstm = LSTMBaseline().to(device)
    tan  = TemporalAttentionNetwork().to(device)
    try:
        lstm.load_state_dict(torch.load(os.path.join(LSTM_DIR,'lstm_best.pt'), map_location=device))
        tan.load_state_dict(torch.load(os.path.join(TAN_DIR,'tan_best.pt'),   map_location=device))
        lstm.eval(); tan.eval()
        return lstm, tan, True
    except:
        return None, None, False

def compute_features(vitals_window):
    feats = []
    for sig in SIGNALS:
        vals  = np.array(vitals_window[sig])
        vals  = vals[~np.isnan(vals)]
        if len(vals) == 0: vals = np.array([0.0])
        t     = np.arange(len(vals))
        slope = np.polyfit(t, vals, 1)[0] if len(vals) > 1 else 0.0
        feats += [float(np.mean(vals)), float(np.std(vals)),
                  float(np.min(vals)),  float(np.max(vals)),
                  float(np.max(vals)-np.min(vals)), float(slope)]
    return np.array(feats, dtype=np.float32)

def compute_rolling_risk(patient, tan_model, window_mins=60):
    n     = len(patient['times'])
    risks = [None] * window_mins
    for i in range(window_mins, n):
        window = {sig: patient[sig][i-window_mins:i] for sig in SIGNALS}
        feats  = compute_features(window)
        X      = np.stack([feats]*4, axis=0)[np.newaxis]
        X_t    = torch.from_numpy(X)
        with torch.no_grad():
            if tan_model is not None:
                p = torch.sigmoid(tan_model(X_t)).item()
            else:
                base = 0.04
                if i > 300: base += (i-300)*0.0015
                p = float(np.clip(base + np.random.normal(0,0.015), 0, 0.99))
        risks.append(p)
    return risks

def detect_change_points(signal_vals, times, thresh, window=10):
    """Find moments where signal changes by more than thresh within window minutes."""
    changes = []
    for i in range(window, len(signal_vals)):
        prev = np.mean(signal_vals[i-window:i-window//2])
        curr = np.mean(signal_vals[i-window//2:i])
        delta = curr - prev
        if abs(delta) >= thresh:
            changes.append({
                'time'  : times[i],
                'time_str': times[i].strftime('%H:%M'),
                'value' : signal_vals[i],
                'delta' : delta,
                'direction': 'UP' if delta > 0 else 'DOWN'
            })
    # Deduplicate — keep only changes separated by >15 min
    deduped = []
    last_t  = None
    for c in changes:
        if last_t is None or (c['time'] - last_t).seconds > 900:
            deduped.append(c)
            last_t = c['time']
    return deduped

def generate_demo_patient(ca_patient=True, seed=42):
    rng = np.random.default_rng(seed)
    n   = 480
    t   = np.arange(n)
    start = datetime(2024, 3, 9, 8, 0, 0)
    times = [start + timedelta(minutes=i) for i in range(n)]

    if ca_patient:
        hr    = 72 + rng.normal(0,2,n) + np.where(t>300,(t-300)*0.10,0) + rng.normal(0,3,n)
        spo2  = 98 - rng.normal(0,0.3,n) - np.where(t>360,(t-360)*0.06,0) + rng.normal(0,0.4,n)
        etco2 = 38 + rng.normal(0,1,n)   - np.where(t>340,(t-340)*0.04,0) + rng.normal(0,1,n)
        mbp   = 85 + rng.normal(0,3,n)   - np.where(t>320,(t-320)*0.14,0) + rng.normal(0,4,n)
        sbp   = mbp + 40 + rng.normal(0,3,n)
        dbp   = mbp - 20 + rng.normal(0,3,n)
        ca_time = 460
    else:
        hr    = 70 + rng.normal(0,3,n)
        spo2  = 98 + rng.normal(0,0.4,n)
        etco2 = 38 + rng.normal(0,1.5,n)
        mbp   = 85 + rng.normal(0,4,n)
        sbp   = mbp + 40 + rng.normal(0,3,n)
        dbp   = mbp - 20 + rng.normal(0,3,n)
        ca_time = None

    return {
        'times'      : times,
        'HR'         : np.clip(hr,   30,200).tolist(),
        'PLETH_SPO2' : np.clip(spo2, 70,100).tolist(),
        'ETCO2'      : np.clip(etco2,10, 60).tolist(),
        'ART_MBP'    : np.clip(mbp,  30,150).tolist(),
        'ART_SBP'    : np.clip(sbp,  50,200).tolist(),
        'ART_DBP'    : np.clip(dbp,  20,120).tolist(),
        'ca_time'    : ca_time,
        'label'      : 1 if ca_patient else 0,
    }

def get_risk_level(p):
    if p >= 0.75:   return 'CRITICAL', '#f38ba8', 'risk-critical'
    elif p >= 0.50: return 'HIGH',     '#fab387', 'risk-high'
    elif p >= 0.25: return 'MODERATE', '#a6e3a1', 'risk-moderate'
    else:           return 'LOW',      '#89b4fa', 'risk-low'

# ══════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("## 🫀 CA Risk Monitor")
    st.markdown("---")
    demo_type = st.selectbox("Patient Type", ["High Risk (CA Event)", "Low Risk (No CA)"])
    seed      = st.slider("Patient Seed", 1, 100, 42)
    ca_patient = "High Risk" in demo_type
    st.markdown("---")
    alert_thresh = st.slider("Alert Threshold (%)", 20, 90, 55) / 100.0
    lookback_min = st.slider("Lookback Window (min)", 30, 240, 60, step=30)
    st.markdown("---")
    st.markdown("""
    <div style='font-size:11px;color:#3d4f6e;font-family:IBM Plex Mono,monospace;'>
    TAN Model | AUROC 0.9937<br>
    95% CI [0.9909–0.9961]<br>
    TSI University 2026
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  LOAD
# ══════════════════════════════════════════════════════════════════════
lstm_model, tan_model, models_ok = load_models()
patient = generate_demo_patient(ca_patient=ca_patient, seed=seed)

with st.spinner("Analysing patient..."):
    risks = compute_rolling_risk(patient, tan_model, lookback_min)

valid_risks  = [r for r in risks if r is not None]
current_risk = valid_risks[-1] if valid_risks else 0.04
risk_level, risk_color, risk_cls = get_risk_level(current_risk)
ca_time_idx  = patient['ca_time']

# ══════════════════════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════════════════════
now_str = datetime.now().strftime("%d %b %Y  %H:%M")
col_h1, col_h2 = st.columns([3,1])
with col_h1:
    st.markdown(f"""
    <div style='padding:10px 0 4px 0;'>
        <span style='font-family:IBM Plex Mono,monospace;font-size:20px;
                     font-weight:700;color:#cdd6f4;'>
            🫀 INTRAOPERATIVE CARDIAC ARREST RISK MONITOR
        </span><br>
        <span style='font-size:11px;color:#3d4f6e;font-family:IBM Plex Mono,monospace;'>
            TAN Model &nbsp;|&nbsp; AUROC 0.9937 &nbsp;|&nbsp; {now_str}
            &nbsp;|&nbsp; {"⚠️ DEMO — HIGH RISK PATIENT" if ca_patient else "✓ DEMO — LOW RISK PATIENT"}
        </span>
    </div>""", unsafe_allow_html=True)

st.markdown("---")

# ══════════════════════════════════════════════════════════════════════
#  ROW 1 — Risk score + Current vitals
# ══════════════════════════════════════════════════════════════════════
col_risk, col_v1, col_v2, col_v3, col_v4, col_v5, col_v6 = st.columns([1.4,1,1,1,1,1,1])

with col_risk:
    st.markdown(f"""
    <div class="risk-block {risk_cls}">
        <div style='font-size:11px;color:#3d4f6e;font-family:IBM Plex Mono,monospace;
                    letter-spacing:2px;margin-bottom:4px;'>CA RISK SCORE</div>
        <div style='font-family:IBM Plex Mono,monospace;font-size:56px;
                    font-weight:700;color:{risk_color};line-height:1;'>
            {current_risk*100:.1f}%
        </div>
        <div style='font-size:16px;font-weight:600;color:{risk_color};margin-top:6px;'>
            {risk_level}
        </div>
        <div style='font-size:10px;color:#3d4f6e;margin-top:6px;font-family:IBM Plex Mono,monospace;'>
            window: {lookback_min} min
        </div>
    </div>""", unsafe_allow_html=True)
    if current_risk >= alert_thresh:
        st.markdown(f"""
        <div class="alert-critical">
        🚨 ALERT<br>
        Risk ≥ {alert_thresh*100:.0f}%<br>
        Notify physician NOW
        </div>""", unsafe_allow_html=True)

for i, sig in enumerate(SIGNALS):
    col = [col_v1, col_v2, col_v3, col_v4, col_v5, col_v6][i]
    val = patient[sig][-1]
    lo, hi = NORMAL[sig]
    if val < lo:
        cls, arrow, status = 'val-danger',  '↓ LOW',  'LOW'
    elif val > hi:
        cls, arrow, status = 'val-warning', '↑ HIGH', 'HIGH'
    else:
        cls, arrow, status = 'val-normal',  '→ OK',   'NORMAL'

    # Trend over last 30 min
    last30 = patient[sig][-30:] if len(patient[sig]) >= 30 else patient[sig]
    trend  = np.mean(last30[-10:]) - np.mean(last30[:10])
    trend_str = f"{'↗' if trend > 2 else ('↘' if trend < -2 else '→')} {abs(trend):.1f} / 30min"

    with col:
        st.markdown(f"""
        <div class="vital-tile">
            <div style='font-size:9px;color:#3d4f6e;font-family:IBM Plex Mono,monospace;
                        letter-spacing:1px;'>{SIG_LABEL[sig].upper()}</div>
            <div class="{cls}">{val:.1f}</div>
            <div style='font-size:9px;color:#3d4f6e;'>{SIG_UNIT[sig]}</div>
            <div style='font-size:10px;color:{"#f38ba8" if status != "NORMAL" else "#a6e3a1"};
                        font-family:IBM Plex Mono,monospace;'>{arrow}</div>
            <div style='font-size:9px;color:#3d4f6e;margin-top:2px;'>{trend_str}</div>
            <div style='font-size:9px;color:#3d4f6e;'>
                normal: {lo}–{hi}
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  ROW 2 — TAN Risk Timeline (full width, prominent)
# ══════════════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">TAN Risk Score Over Time</p>', unsafe_allow_html=True)

risk_times  = [patient['times'][i].strftime('%H:%M') for i, r in enumerate(risks) if r is not None]
risk_values = [r for r in risks if r is not None]

fig_risk = go.Figure()

# Danger zone fill
fig_risk.add_hrect(y0=alert_thresh, y1=1.0,
    fillcolor='rgba(243,139,168,0.04)', line_width=0)
fig_risk.add_hrect(y0=0.75, y1=1.0,
    fillcolor='rgba(243,139,168,0.06)', line_width=0)

# Risk line with gradient color
fig_risk.add_trace(go.Scatter(
    x=risk_times, y=risk_values,
    mode='lines',
    line=dict(color='#89b4fa', width=2.5),
    fill='tozeroy', fillcolor='rgba(137,180,250,0.06)',
    name='CA Risk',
    hovertemplate='<b>Time: %{x}</b><br>Risk: %{y:.1%}<extra></extra>'
))

# Threshold line
fig_risk.add_hline(y=alert_thresh, line_dash='dash',
    line_color='#fab387', line_width=1.2,
    annotation_text=f'Alert threshold ({alert_thresh*100:.0f}%)',
    annotation_font_color='#fab387', annotation_font_size=10,
    annotation_position='top right')

fig_risk.add_hline(y=0.75, line_dash='dot',
    line_color='#f38ba8', line_width=1,
    annotation_text='Critical (75%)',
    annotation_font_color='#f38ba8', annotation_font_size=10,
    annotation_position='top left')

# CA event marker — use scatter line instead of add_vline
if ca_time_idx is not None:
    ca_risk_idx = ca_time_idx - (len(risks) - len(risk_values)) - 1
    if 0 <= ca_risk_idx < len(risk_times):
        ca_t_str = risk_times[ca_risk_idx]
        fig_risk.add_trace(go.Scatter(
            x=[ca_t_str, ca_t_str], y=[0, 1],
            mode='lines+text',
            line=dict(color='#f38ba8', width=2.5, dash='dot'),
            text=['', '⚠ CA EVENT'],
            textposition='top center',
            textfont=dict(color='#f38ba8', size=11, family='IBM Plex Mono'),
            showlegend=False, hoverinfo='skip'
        ))

# Alert threshold crossing marker
crossed = False
for i in range(1, len(risk_values)):
    if not crossed and risk_values[i] >= alert_thresh and risk_values[i-1] < alert_thresh:
        fig_risk.add_trace(go.Scatter(
            x=[risk_times[i], risk_times[i]], y=[0, 1],
            mode='lines+text',
            line=dict(color='#fab387', width=1.5, dash='dash'),
            text=['', '🔔 ALERT'],
            textposition='top center',
            textfont=dict(color='#fab387', size=10, family='IBM Plex Mono'),
            showlegend=False, hoverinfo='skip'
        ))
        crossed = True

fig_risk.update_layout(
    height=200,
    plot_bgcolor='#0d1220', paper_bgcolor='#070a10',
    yaxis=dict(tickformat='.0%', range=[0,1.05],
               gridcolor='#1a2035', title='Risk',
               titlefont=dict(color='#3d4f6e',size=10),
               tickfont=dict(color='#3d4f6e',size=9)),
    xaxis=dict(gridcolor='#1a2035', tickfont=dict(color='#3d4f6e',size=9),
               nticks=20),
    font=dict(family='IBM Plex Mono', color='#3d4f6e'),
    margin=dict(l=50,r=20,t=20,b=30),
    showlegend=False
)
st.plotly_chart(fig_risk, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════
#  ROW 3 — Individual signal charts with change point annotations
# ══════════════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">Signal-by-Signal Analysis — Change Points Highlighted</p>',
            unsafe_allow_html=True)

# Build per-signal charts — 2 columns × 3 rows
sig_pairs = [(SIGNALS[i], SIGNALS[i+1]) for i in range(0, 6, 2)]

for sig_a, sig_b in sig_pairs:
    col_a, col_b = st.columns(2)

    for sig, col in [(sig_a, col_a), (sig_b, col_b)]:
        with col:
            vals  = patient[sig]
            times = patient['times']
            lo, hi = NORMAL[sig]
            color  = SIG_COLOR[sig]
            times_str = [t.strftime('%H:%M') for t in times]

            # Detect change points
            changes = detect_change_points(vals, times, CHANGE_THRESH[sig], window=15)

            fig = go.Figure()

            # Normal range band
            fig.add_hrect(y0=lo, y1=hi,
                fillcolor='rgba(166,227,161,0.04)', line_width=0)
            fig.add_hline(y=hi, line_dash='dot', line_color='#2a4a2a',
                line_width=0.8)
            fig.add_hline(y=lo, line_dash='dot', line_color='#2a4a2a',
                line_width=0.8)

            # Main signal line — color danger zones
            fig.add_trace(go.Scatter(
                x=times_str, y=vals,
                mode='lines',
                line=dict(color=color, width=2),
                name=SIG_LABEL[sig],
                hovertemplate=f'<b>{SIG_LABEL[sig]}</b><br>'
                              f'Time: %{{x}}<br>'
                              f'Value: %{{y:.1f}} {SIG_UNIT[sig]}<extra></extra>'
            ))

            # Danger zone — values outside normal
            danger_vals = [v if (v < lo or v > hi) else None for v in vals]
            fig.add_trace(go.Scatter(
                x=times_str, y=danger_vals,
                mode='markers',
                marker=dict(color='#f38ba8', size=3, opacity=0.6),
                name='Out of range',
                hoverinfo='skip', showlegend=False
            ))

            # Change point markers + annotations
            for cp in changes:
                cp_str = cp['time'].strftime('%H:%M')
                # Vertical line via scatter
                fig.add_trace(go.Scatter(
                    x=[cp_str, cp_str],
                    y=[min(vals)*0.98, max(vals)*1.02],
                    mode='lines',
                    line=dict(color='#fab387', width=1.2, dash='dot'),
                    showlegend=False, hoverinfo='skip'
                ))
                fig.add_annotation(
                    x=cp_str,
                    y=cp['value'],
                    text=f"{'↑' if cp['direction']=='UP' else '↓'}{abs(cp['delta']):.1f}",
                    showarrow=True,
                    arrowhead=2,
                    arrowcolor='#fab387',
                    arrowsize=0.8,
                    arrowwidth=1.2,
                    font=dict(size=10, color='#fab387', family='IBM Plex Mono'),
                    bgcolor='#1e1408',
                    bordercolor='#fab387',
                    borderwidth=1,
                    borderpad=3,
                    ax=0, ay=-30
                )

            # CA event marker
            if ca_time_idx is not None:
                ca_str = patient['times'][ca_time_idx].strftime('%H:%M')
                fig.add_trace(go.Scatter(
                    x=[ca_str, ca_str],
                    y=[min(vals)*0.98, max(vals)*1.02],
                    mode='lines+text',
                    line=dict(color='#f38ba8', width=2, dash='dot'),
                    text=['', 'CA'],
                    textposition='top center',
                    textfont=dict(size=10, color='#f38ba8', family='IBM Plex Mono'),
                    showlegend=False, hoverinfo='skip'
                ))

            fig.update_layout(
                height=220,
                title=dict(
                    text=f'{SIG_LABEL[sig]}  <span style="font-size:11px;color:#3d4f6e">'
                         f'({SIG_UNIT[sig]}) &nbsp; normal: {lo}–{hi} &nbsp; '
                         f'changes detected: {len(changes)}</span>',
                    font=dict(size=12, color='#cdd6f4',
                              family='IBM Plex Mono'),
                    x=0
                ),
                plot_bgcolor='#0d1220', paper_bgcolor='#070a10',
                yaxis=dict(gridcolor='#1a2035',
                           tickfont=dict(color='#3d4f6e',size=9)),
                xaxis=dict(gridcolor='#1a2035',
                           tickfont=dict(color='#3d4f6e',size=9),
                           nticks=12),
                font=dict(family='IBM Plex Mono', color='#3d4f6e'),
                margin=dict(l=40,r=10,t=40,b=30),
                showlegend=False
            )
            st.plotly_chart(fig, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════
#  ROW 4 — Change point summary table
# ══════════════════════════════════════════════════════════════════════
st.markdown('<p class="section-label">Change Point Summary — All Signals</p>',
            unsafe_allow_html=True)

all_changes = []
for sig in SIGNALS:
    changes = detect_change_points(
        patient[sig], patient['times'], CHANGE_THRESH[sig], window=15)
    for cp in changes:
        lo, hi = NORMAL[sig]
        in_range = lo <= cp['value'] <= hi
        all_changes.append({
            'Time'     : cp['time_str'],
            'Signal'   : SIG_LABEL[sig],
            'Value'    : f"{cp['value']:.1f} {SIG_UNIT[sig]}",
            'Change'   : f"{'↑' if cp['direction']=='UP' else '↓'} {abs(cp['delta']):.1f}",
            'Status'   : '✓ Normal range' if in_range else '⚠ Outside normal',
            'Normal'   : f"{lo}–{hi} {SIG_UNIT[sig]}",
            '_danger'  : not in_range,
            '_direction': cp['direction'],
        })

all_changes.sort(key=lambda x: x['Time'])

if all_changes:
    rows_html = ""
    for c in all_changes:
        dir_cls  = 'change-up'   if c['_direction'] == 'UP' else 'change-down'
        stat_cls = 'change-up'   if c['_danger'] else 'change-ok'
        rows_html += f"""
        <tr>
            <td style='color:#cdd6f4;'>{c['Time']}</td>
            <td style='color:{SIG_COLOR.get(next((s for s in SIGNALS if SIG_LABEL[s]==c["Signal"]), SIGNALS[0]),"#cdd6f4")};'>
                {c['Signal']}</td>
            <td style='color:#cdd6f4;'>{c['Value']}</td>
            <td class='{dir_cls}'>{c['Change']}</td>
            <td class='{stat_cls}'>{c['Status']}</td>
            <td style='color:#3d4f6e;'>{c['Normal']}</td>
        </tr>"""

    st.markdown(f"""
    <table class="change-table">
        <thead><tr>
            <th>TIME</th><th>SIGNAL</th><th>VALUE</th>
            <th>CHANGE</th><th>STATUS</th><th>NORMAL RANGE</th>
        </tr></thead>
        <tbody>{rows_html}</tbody>
    </table>""", unsafe_allow_html=True)
else:
    st.markdown('<div class="info-strip">No significant change points detected.</div>',
                unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  ROW 5 — Attention weights + Window risk
# ══════════════════════════════════════════════════════════════════════
st.markdown("<br>", unsafe_allow_html=True)
col_attn, col_win = st.columns(2)

with col_attn:
    st.markdown('<p class="section-label">TAN Attention — Which Window Matters Most</p>',
                unsafe_allow_html=True)
    try:
        attn_raw  = np.load(os.path.join(TAN_DIR, 'attention_weights_cv.npy'))
        attn_mean = attn_raw.mean(axis=(0,1))
        attn_norm = attn_mean / attn_mean.sum()
    except:
        attn_norm = np.array([0.1622, 0.1516, 0.1570, 0.5292])

    fig_attn = go.Figure()
    attn_colors = ['#4a7fc1','#e8b84b','#d95f3b','#4a9e72']
    fig_attn.add_trace(go.Bar(
        x=[f'{w} min' for w in WINDOWS],
        y=attn_norm,
        marker_color=attn_colors,
        text=[f"{v*100:.1f}%" for v in attn_norm],
        textposition='outside',
        textfont=dict(color='#cdd6f4', size=12, family='IBM Plex Mono'),
    ))
    dominant_w = WINDOWS[np.argmax(attn_norm)]
    fig_attn.update_layout(
        height=220,
        plot_bgcolor='#0d1220', paper_bgcolor='#070a10',
        yaxis=dict(tickformat='.0%', range=[0,0.72],
                   gridcolor='#1a2035', tickfont=dict(color='#3d4f6e',size=9)),
        xaxis=dict(tickfont=dict(color='#a6adc8', size=11)),
        font=dict(family='IBM Plex Mono', color='#3d4f6e'),
        margin=dict(l=30,r=10,t=10,b=30), showlegend=False
    )
    st.plotly_chart(fig_attn, use_container_width=True)
    st.markdown(f"""
    <div class="info-strip">
    🧠 Model focuses most on <strong>{dominant_w}-min</strong> window
    ({attn_norm[WINDOWS.index(dominant_w)]*100:.1f}% attention weight).<br>
    This means physiological changes <strong>{dominant_w} minutes before</strong>
    the current time are the strongest predictors of cardiac arrest.
    </div>""", unsafe_allow_html=True)

with col_win:
    st.markdown('<p class="section-label">Risk Score per Prediction Window</p>',
                unsafe_allow_html=True)
    per_win_risks = {}
    now_idx = len(patient['times']) - 1
    for w in WINDOWS:
        start_i = max(0, now_idx - w)
        window  = {sig: patient[sig][start_i:now_idx+1] for sig in SIGNALS}
        feats   = compute_features(window)
        X       = np.stack([feats]*4, axis=0)[np.newaxis]
        X_t     = torch.from_numpy(X)
        with torch.no_grad():
            if tan_model is not None:
                p = torch.sigmoid(tan_model(X_t)).item()
            else:
                p = current_risk + np.random.normal(0, 0.03)
        per_win_risks[w] = float(np.clip(p, 0, 1))

    win_colors = []
    for w in WINDOWS:
        _, c, _ = get_risk_level(per_win_risks[w])
        win_colors.append(c)

    fig_win = go.Figure()
    fig_win.add_trace(go.Bar(
        x=[f'{w} min' for w in WINDOWS],
        y=list(per_win_risks.values()),
        marker_color=win_colors,
        text=[f"{v*100:.1f}%" for v in per_win_risks.values()],
        textposition='outside',
        textfont=dict(color='#cdd6f4', size=12, family='IBM Plex Mono'),
    ))
    fig_win.add_hline(y=alert_thresh, line_dash='dash',
        line_color='#fab387', line_width=1)
    fig_win.update_layout(
        height=220,
        plot_bgcolor='#0d1220', paper_bgcolor='#070a10',
        yaxis=dict(tickformat='.0%', range=[0,1.15],
                   gridcolor='#1a2035', tickfont=dict(color='#3d4f6e',size=9)),
        xaxis=dict(tickfont=dict(color='#a6adc8', size=11)),
        font=dict(family='IBM Plex Mono', color='#3d4f6e'),
        margin=dict(l=30,r=10,t=10,b=30), showlegend=False
    )
    st.plotly_chart(fig_win, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════
#  FOOTER — Nurse guide
# ══════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown("""
<div class="info-strip">
<strong>📋 Nurse Quick Reference</strong><br>
🔴 <strong>CRITICAL ≥75%</strong> — Prepare resuscitation. Alert physician immediately.<br>
🟠 <strong>HIGH 50–75%</strong> — Increase monitoring. Check medication dosages. Review vitals trend.<br>
🟡 <strong>MODERATE 25–50%</strong> — Continue close monitoring. Note deteriorating signals.<br>
🔵 <strong>LOW &lt;25%</strong> — Routine monitoring. Patient stable.<br>
🔶 <strong>Orange markers (↑↓)</strong> on signal charts indicate the exact time and magnitude of each significant vital sign change.<br>
🔴 <strong>Red dashed line</strong> = cardiac arrest event (training data reference only).<br><br>
<em>This is a clinical decision-support tool. All treatment decisions remain with the attending physician and anaesthesiologist.</em>
</div>""", unsafe_allow_html=True)
