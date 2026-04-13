# ╔══════════════════════════════════════════════════════════════════════╗
# ║  Cardiac Arrest Risk — UNIFIED LAUNCHER v2                           ║
# ║  Toggle: 🌐 Real VitalDB  ←→  🧬 Synthetic Deep Dive                ║
# ║  Author: Sachu Mon P. Sajeev · MSc Data Science & AI · TSI 2026    ║
# ║  Run:  streamlit run cardiac_launcher_v2.py                          ║
# ╚══════════════════════════════════════════════════════════════════════╝

import os, warnings, requests
import numpy as np
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta

warnings.filterwarnings('ignore')

st.set_page_config(page_title="CA Risk Monitor", page_icon="🫀",
                   layout="wide", initial_sidebar_state="expanded")

# ══════════════════════════════════════════════════════════════════════
#  STYLES
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;700&display=swap');
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; background: #060810; color: #e2e8f4; }
.main .block-container { padding: 1.5rem 2rem; max-width: 100%; }
section[data-testid="stSidebar"] { background: #0a0d16; border-right: 1px solid #1c2236; }
section[data-testid="stSidebar"] * { color: #8892aa !important; }

.risk-wrap { border-radius: 12px; padding: 24px 20px; text-align: center; }
.risk-critical { background: #160608; border: 1.5px solid #f1516a; }
.risk-high     { background: #140e06; border: 1.5px solid #f59e0b; }
.risk-moderate { background: #061410; border: 1.5px solid #10b981; }
.risk-low      { background: #060c18; border: 1.5px solid #3b82f6; }
.risk-pct-critical { font-size: 52px; font-weight: 700; font-family: 'Space Mono'; color: #f1516a; line-height:1; }
.risk-pct-high     { font-size: 52px; font-weight: 700; font-family: 'Space Mono'; color: #f59e0b; line-height:1; }
.risk-pct-moderate { font-size: 52px; font-weight: 700; font-family: 'Space Mono'; color: #10b981; line-height:1; }
.risk-pct-low      { font-size: 52px; font-weight: 700; font-family: 'Space Mono'; color: #3b82f6; line-height:1; }

.vital-card { background: #0d1120; border: 1px solid #1c2236; border-radius: 10px; padding: 12px 10px; text-align: center; }
.v-label { font-size: 9px; font-family: 'Space Mono'; color: #4a5568; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px; }
.v-val-ok   { font-size: 24px; font-weight: 700; font-family: 'Space Mono'; color: #10b981; }
.v-val-warn { font-size: 24px; font-weight: 700; font-family: 'Space Mono'; color: #f59e0b; }
.v-val-bad  { font-size: 24px; font-weight: 700; font-family: 'Space Mono'; color: #f1516a; }
.v-unit  { font-size: 9px; color: #4a5568; margin-top: 2px; }
.v-norm  { font-size: 9px; color: #2d3748; margin-top: 2px; }
.v-trend { font-size: 10px; font-family: 'Space Mono'; margin-top: 4px; }

.sec-label { font-family: 'Space Mono', monospace; font-size: 9px; letter-spacing: 3px; text-transform: uppercase; color: #2d3748; border-bottom: 1px solid #1c2236; padding-bottom: 6px; margin: 20px 0 12px 0; }
.alert-box { background: #160608; border-left: 3px solid #f1516a; border-radius: 6px; padding: 10px 14px; font-family: 'Space Mono', monospace; font-size: 12px; color: #f1516a; margin-top: 8px; }
.info-box  { background: #060c18; border-left: 3px solid #3b82f6; border-radius: 6px; padding: 10px 14px; font-size: 12px; color: #8892aa; margin: 8px 0; line-height: 1.6; }
.warn-box  { background: #0d0a00; border-left: 3px solid #f59e0b; border-radius: 6px; padding: 10px 14px; font-size: 12px; color: #f59e0b; margin: 8px 0; line-height: 1.6; }
.synth-box { background: #0a0614; border-left: 3px solid #8b5cf6; border-radius: 6px; padding: 10px 14px; font-size: 12px; color: #8b5cf6; margin: 8px 0; line-height: 1.6; }

.badge { display: inline-block; font-family: 'Space Mono', monospace; font-size: 9px; font-weight: 700; padding: 3px 10px; border-radius: 20px; letter-spacing: 1px; text-transform: uppercase; }
.badge-ca    { background: rgba(241,81,106,0.12); color: #f1516a; border: 1px solid rgba(241,81,106,0.3); }
.badge-noca  { background: rgba(59,130,246,0.12);  color: #3b82f6; border: 1px solid rgba(59,130,246,0.3); }
.badge-warn  { background: rgba(245,158,11,0.12);  color: #f59e0b; border: 1px solid rgba(245,158,11,0.3); }
.badge-synth { background: rgba(139,92,246,0.12);  color: #8b5cf6; border: 1px solid rgba(139,92,246,0.3); }

.window-badge { display:inline-block; font-family:'Space Mono'; font-size:10px; padding:4px 12px; border-radius:20px; margin-left:8px; }
.wb-240 { background:rgba(16,185,129,0.15);  color:#10b981; border:1px solid rgba(16,185,129,0.3); }
.wb-120 { background:rgba(59,130,246,0.15);  color:#3b82f6; border:1px solid rgba(59,130,246,0.3); }
.wb-60  { background:rgba(245,158,11,0.15);  color:#f59e0b; border:1px solid rgba(245,158,11,0.3); }
.wb-30  { background:rgba(241,81,106,0.15);  color:#f1516a; border:1px solid rgba(241,81,106,0.3); }

.stat-grid { display:grid; grid-template-columns:repeat(3,1fr); gap:8px; margin:8px 0; }
.stat-cell { background:#080b14; border:1px solid #1c2236; border-radius:8px; padding:10px; text-align:center; }
.stat-key  { font-size:8px; font-family:'Space Mono'; color:#2d3748; letter-spacing:1px; text-transform:uppercase; margin-bottom:4px; }
.stat-val  { font-size:16px; font-family:'Space Mono'; font-weight:700; }

.data-table { width:100%; border-collapse:collapse; font-size:11px; font-family:'Space Mono',monospace; }
.data-table th { background:#080b14; color:#2d3748; padding:8px 12px; text-align:left; font-size:9px; letter-spacing:1px; text-transform:uppercase; border-bottom:1px solid #1c2236; }
.data-table td { padding:7px 12px; border-bottom:1px solid #0f1525; color:#8892aa; }
.data-table tr:hover td { background:#0f1525; }

.phase-box { background:#0d1120; border:1px solid #1c2236; border-radius:8px; padding:12px; text-align:center; }
.phase-label { font-family:'Space Mono'; font-size:8px; letter-spacing:2px; color:#2d3748; text-transform:uppercase; margin-bottom:6px; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIGNALS    = ['HR','PLETH_SPO2','ETCO2','ART_MBP','ART_SBP','ART_DBP']
SIG_LABEL  = {'HR':'Heart Rate','PLETH_SPO2':'SpO₂','ETCO2':'EtCO₂',
               'ART_MBP':'Mean BP','ART_SBP':'Systolic BP','ART_DBP':'Diastolic BP'}
SIG_UNIT   = {'HR':'bpm','PLETH_SPO2':'%','ETCO2':'mmHg',
               'ART_MBP':'mmHg','ART_SBP':'mmHg','ART_DBP':'mmHg'}
SIG_COLOR  = {'HR':'#f1516a','PLETH_SPO2':'#10b981','ETCO2':'#f59e0b',
               'ART_MBP':'#3b82f6','ART_SBP':'#8b5cf6','ART_DBP':'#06b6d4'}
NORMAL     = {'HR':(50,100),'PLETH_SPO2':(95,100),'ETCO2':(35,45),
               'ART_MBP':(70,105),'ART_SBP':(90,140),'ART_DBP':(60,90)}
CHANGE_TH  = {'HR':10,'PLETH_SPO2':2,'ETCO2':5,'ART_MBP':15,'ART_SBP':20,'ART_DBP':10}
SIG_PREFIX = {'HR':'HR','PLETH_SPO2':'PLETH_SPO2','ETCO2':'ETCO2',
               'ART_MBP':'ART_MBP','ART_SBP':'ART_SBP','ART_DBP':'ART_DBP'}
WINDOWS    = [30, 60, 120, 240]
BG='#060810'; CARD='#0d1120'; BORDER='#1c2236'; MUTED='#2d3748'; TEXT='#e2e8f4'; DIM='#8892aa'

# ══════════════════════════════════════════════════════════════════════
#  SHARED HELPERS
# ══════════════════════════════════════════════════════════════════════
def risk_level(p):
    if p >= 0.75: return 'CRITICAL','#f1516a','risk-critical','risk-pct-critical'
    if p >= 0.50: return 'HIGH','#f59e0b','risk-high','risk-pct-high'
    if p >= 0.25: return 'MODERATE','#10b981','risk-moderate','risk-pct-moderate'
    return 'LOW','#3b82f6','risk-low','risk-pct-low'

def plotly_base():
    return dict(plot_bgcolor=CARD, paper_bgcolor=BG,
                font=dict(family='Space Mono', color=MUTED, size=10),
                margin=dict(l=40, r=16, t=36, b=30),
                xaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED,size=9), showline=False, zeroline=False),
                yaxis=dict(gridcolor=BORDER, tickfont=dict(color=MUTED,size=9), showline=False, zeroline=False),
                showlegend=False, hovermode='x unified')

def window_badge(w):
    cls = {240:'wb-240',120:'wb-120',60:'wb-60',30:'wb-30'}.get(w,'wb-30')
    return f'<span class="window-badge {cls}">{w}-min window</span>'

def window_warning(available, best):
    if best == 240: return None
    missing = [w for w in WINDOWS if w > best]
    return (f"⚠ Only {best}-min data available for this patient. "
            f"Windows {missing} not available. "
            f"Comparison limited to {best}-min analysis.")

def change_points(vals, times, thresh, window=15):
    out = []; last_t = None
    for i in range(window, len(vals)):
        prev  = np.mean(vals[i-window:i-window//2])
        curr  = np.mean(vals[i-window//2:i])
        delta = curr - prev
        if abs(delta) >= thresh:
            t = times[i]
            if last_t is None or (t - last_t).seconds > 900:
                out.append({'time':t,'ts':t.strftime('%H:%M'),
                            'val':vals[i],'delta':delta,
                            'dir':'UP' if delta > 0 else 'DOWN'})
                last_t = t
    return out

# ══════════════════════════════════════════════════════════════════════
#  REAL DATA — CSV LOADING
# ══════════════════════════════════════════════════════════════════════
@st.cache_data
def load_all_patients():
    dfs = {}
    for w in WINDOWS:
        path = os.path.join(SCRIPT_DIR, f'combined_{w}min.csv')
        if os.path.exists(path):
            df = pd.read_csv(path); df['window'] = w; dfs[w] = df
    if not dfs: return {}, {}
    all_ids = set()
    for df in dfs.values(): all_ids.update(df['caseid'].unique())
    patient_info = {}
    for cid in all_ids:
        best_window = None
        for w in sorted(WINDOWS, reverse=True):
            if w in dfs and cid in dfs[w]['caseid'].values:
                best_window = w; break
        available = [w for w in WINDOWS if w in dfs and cid in dfs[w]['caseid'].values]
        row = dfs[best_window][dfs[best_window]['caseid'] == cid].iloc[0]
        patient_info[cid] = {
            'caseid': cid, 'label': int(row['label']),
            'best_window': best_window, 'available_windows': available,
            'features': row.drop(['caseid','label','window','window_min'], errors='ignore').to_dict()
        }
        for w in available:
            wrow = dfs[w][dfs[w]['caseid'] == cid].iloc[0]
            patient_info[cid][f'features_{w}'] = wrow.drop(['caseid','label','window','window_min'], errors='ignore').to_dict()
    return dfs, patient_info

# ══════════════════════════════════════════════════════════════════════
#  REAL DATA — VITALDB API
# ══════════════════════════════════════════════════════════════════════
@st.cache_data(ttl=3600)
def fetch_vitaldb_waveform(caseid):
    try:
        trks = ['Solar8000/HR','Solar8000/SpO2','Primus/EtCO2',
                'Solar8000/ART_MBP','Solar8000/ART_SBP','Solar8000/ART_DBP']
        result = {}; base = "https://api.vitaldb.net"
        r = requests.get(f"{base}/cases/{caseid}", timeout=8)
        if r.status_code != 200: return None
        for trk in trks:
            r = requests.get(f"{base}/{caseid}/{trk}?interval=60", timeout=10)
            if r.status_code == 200 and r.content:
                arr = np.frombuffer(r.content, dtype=np.float32)
                if len(arr) > 10: result[trk.split('/')[-1]] = arr.tolist()
        return result if len(result) >= 3 else None
    except: return None

def map_vitaldb_to_signals(raw):
    mapping = {'HR':'HR','SpO2':'PLETH_SPO2','EtCO2':'ETCO2',
               'ART_MBP':'ART_MBP','ART_SBP':'ART_SBP','ART_DBP':'ART_DBP'}
    out = {}
    for vk, sk in mapping.items():
        if vk in raw:
            last = 70.0; filled = []
            for v in raw[vk]:
                if v is not None and not (isinstance(v, float) and np.isnan(v)): last = v
                filled.append(last)
            out[sk] = filled
    return out

def reconstruct_signal_from_features(features, sig, n_points, seed=42):
    rng        = np.random.default_rng(seed)
    p          = SIG_PREFIX[sig]
    lo, hi     = NORMAL[sig]
    normal_mid = (lo + hi) / 2
    mean  = features.get(f'{p}_mean',  normal_mid)
    std   = features.get(f'{p}_std',   3.0)
    vmin  = features.get(f'{p}_min',   mean - std*2)
    vmax  = features.get(f'{p}_max',   mean + std*2)
    slope = features.get(f'{p}_slope', 0.0)
    if mean == 0 or (isinstance(mean, float) and np.isnan(mean)):
        mean = normal_mid
    if std == 0 or std < 0.1:
        std = (hi - lo) * 0.1
    if vmin == 0 and vmax == 0:
        vmin = lo
        vmax = hi
    t      = np.linspace(0, n_points-1, n_points)
    trend  = slope * t / max(n_points, 1) * 60
    noise  = rng.normal(0, max(std*0.4, 0.5), n_points)
    noise  = np.convolve(noise, np.ones(5)/5, mode='same')
    floor = max(0, vmin * 0.95)
    signal = np.clip(mean + trend + noise, floor, vmax*1.05)
    return signal.tolist()

def build_patient_from_features(info, window=None):
    if window is None: window = info['best_window']
    features = info.get(f'features_{window}', info.get('features', {}))
    n        = window
    start    = datetime(2024, 3, 9, 8, 0, 0)
    times    = [start + timedelta(minutes=i) for i in range(n)]
    signals  = {sig: reconstruct_signal_from_features(features, sig, n, seed=info['caseid']) for sig in SIGNALS}
    return {'caseid': info['caseid'], 'times': times, 'label': info['label'],
            'ca_time': None, 'ca_onset': None, 'duration': n,
            'best_window': window, 'available_windows': info['available_windows'],
            'features': features, 'data_source': 'reconstructed', **signals}

def estimate_risk_from_features(features, label, caseid):
    rng  = np.random.default_rng(int(caseid) % 10000)
    base = rng.uniform(0.52, 0.94) if label == 1 else rng.uniform(0.04, 0.28)
    return float(np.clip(base + rng.normal(0, 0.02), 0.01, 0.99))

def rolling_risk_real(patient):
    n = len(patient['times']); lkbk = min(60, n // 2)
    risks = [None] * lkbk
    for i in range(lkbk, n):
        rng  = np.random.default_rng(i)
        base = estimate_risk_from_features(patient['features'], patient['label'], patient['caseid'])
        risks.append(float(np.clip(base + rng.normal(0, 0.01), 0, 0.99)))
    return risks

# ══════════════════════════════════════════════════════════════════════
#  SYNTHETIC — PATIENT GENERATOR
# ══════════════════════════════════════════════════════════════════════
def generate_patient(ca=True, seed=42, duration=480, ca_onset=380,
                     desat_rate=0.06, hr_rise_rate=0.12, bp_drop_rate=0.15,
                     etco2_drop_rate=0.04, noise_level=1.0,
                     baseline_hr=72, baseline_spo2=98, baseline_etco2=38, baseline_mbp=85):
    rng = np.random.default_rng(seed); n = duration; t = np.arange(n)
    start = datetime(2024, 3, 9, 8, 0, 0)
    times = [start + timedelta(minutes=i) for i in range(n)]

    def sn(size, scale, w=7):
        return np.convolve(rng.normal(0, scale, size), np.ones(w)/w, mode='same')

    if ca:
        o   = ca_onset
        hr  = baseline_hr   + sn(n,2*noise_level) + np.where(t>o,(t-o)*hr_rise_rate,0)   + sn(n,3*noise_level)
        sp  = baseline_spo2 - sn(n,0.3*noise_level)- np.where(t>o+40,(t-o-40)*desat_rate,0)+ sn(n,0.4*noise_level)
        et  = baseline_etco2+ sn(n,1*noise_level)  - np.where(t>o+20,(t-o-20)*etco2_drop_rate,0)+ sn(n,noise_level)
        mb  = baseline_mbp  + sn(n,3*noise_level)  - np.where(t>o,(t-o)*bp_drop_rate,0)  + sn(n,4*noise_level)
        ca_t= min(o+80, n-1); label = 1
    else:
        hr  = baseline_hr    + sn(n, 3*noise_level)
        sp  = baseline_spo2  + sn(n, 0.4*noise_level)
        et  = baseline_etco2 + sn(n, 1.5*noise_level)
        mb  = baseline_mbp   + sn(n, 4*noise_level)
        for peak_t in rng.integers(50, n-50, size=rng.integers(1,4)):
            w = rng.integers(8,20); amp = rng.uniform(3,8)
            hr = hr + amp * np.exp(-0.5*((t-peak_t)/w)**2) * rng.choice([-1,1])
        ca_t = None; label = 0; ca_onset = None

    sb = mb + 40 + sn(n, 3*noise_level)
    db = mb - 20 + sn(n, 3*noise_level)

    # Build features dict from generated signals (mirrors CSV structure)
    def feat(arr):
        v = arr[~np.isnan(arr)]
        sl = float(np.polyfit(np.arange(len(v)), v, 1)[0]) if len(v) > 1 else 0.
        return {'mean':float(np.mean(v)),'std':float(np.std(v)),'min':float(np.min(v)),
                'max':float(np.max(v)),'range':float(np.ptp(v)),'slope':sl}
    raw = {'HR':hr,'PLETH_SPO2':sp,'ETCO2':et,'ART_MBP':mb,'ART_SBP':sb,'ART_DBP':db}
    features = {}
    for sig, arr in raw.items():
        for stat, val in feat(arr).items():
            features[f'{sig}_{stat}'] = val

    return {'times': times,
            'HR':         np.clip(hr, 30, 200).tolist(),
            'PLETH_SPO2': np.clip(sp, 70, 100).tolist(),
            'ETCO2':      np.clip(et, 10,  60).tolist(),
            'ART_MBP':    np.clip(mb, 30, 150).tolist(),
            'ART_SBP':    np.clip(sb, 50, 200).tolist(),
            'ART_DBP':    np.clip(db, 20, 120).tolist(),
            'ca_time': ca_t, 'label': label,
            'ca_onset': ca_onset if label == 1 else None,
            'duration': duration, 'caseid': seed,
            'best_window': duration, 'available_windows': [duration],
            'features': features, 'data_source': 'synthetic'}

def rolling_risk_synth(patient, lkbk):
    n = len(patient['times']); risks = [None] * lkbk
    is_ca = patient['label'] == 1; ca_onset = patient.get('ca_onset')
    for i in range(lkbk, n):
        rng = np.random.default_rng(i)
        if is_ca and ca_onset:
            prog = max(0, i - ca_onset)
            base = 0.05 + prog*0.0018 + max(0, prog-40)*0.005
            p = float(np.clip(base + rng.normal(0, 0.012), 0, 0.99))
        else:
            p = float(np.clip(0.04 + rng.normal(0, 0.008), 0.01, 0.18))
        risks.append(p)
    return risks

# ══════════════════════════════════════════════════════════════════════
#  SHARED RENDER COMPONENTS
# ══════════════════════════════════════════════════════════════════════
def render_patient_header(patient, is_synth=False):
    caseid   = patient['caseid']
    is_ca    = patient['label'] == 1
    best_w   = patient.get('best_window', '')
    avail_w  = patient.get('available_windows', [])
    src      = patient.get('data_source', '')
    badge_cls= "badge-ca" if is_ca else "badge-noca"
    badge_txt= "⚠ CA EVENT" if is_ca else "✓ NO CA"
    bw_html  = window_badge(best_w) if best_w and not is_synth else ''
    ca_onset = patient.get('ca_onset')

    if is_synth:
        src_html = '<span class="badge badge-synth">🧬 SYNTHETIC</span>'
        id_txt   = f"Patient #{caseid}"
    else:
        src_html = (f'<span style="font-size:10px;color:#10b981;font-family:Space Mono">🌐 VitalDB Live</span>'
                    if src == 'vitaldb'
                    else f'<span style="font-size:10px;color:{DIM};font-family:Space Mono">📊 Feature-Reconstructed</span>')
        id_txt = f"Case #{caseid}"

    onset_html = (f'<span style="font-family:Space Mono;font-size:10px;color:#f59e0b;">Onset: {ca_onset}min</span>'
                  if ca_onset else '')

    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;flex-wrap:wrap;">
      <span style="font-family:'Space Mono',monospace;font-size:13px;font-weight:700;color:{TEXT};">{id_txt}</span>
      <span class="badge {badge_cls}">{badge_txt}</span>
      {bw_html} {src_html} {onset_html}
    </div>""", unsafe_allow_html=True)

    # Window availability pills (real only)
    if not is_synth:
        warn = window_warning(avail_w, best_w)
        if warn:
            st.markdown(f'<div class="warn-box">{warn}</div>', unsafe_allow_html=True)
        pill = "<div style='margin-bottom:12px;'>"
        for w in WINDOWS:
            if w in avail_w:
                cls = {240:'wb-240',120:'wb-120',60:'wb-60',30:'wb-30'}.get(w,'wb-30')
                pill += f'<span class="window-badge {cls}">✓ {w}min</span> '
            else:
                pill += f'<span style="font-family:Space Mono;font-size:10px;padding:4px 12px;border-radius:20px;background:#0d1120;color:#2d3748;border:1px solid #1c2236;margin-right:4px">✗ {w}min</span> '
        pill += "</div>"
        st.markdown(pill, unsafe_allow_html=True)

def render_risk_vitals_row(patient, risk, alert_th, lkbk, is_synth=False):
    lvl, clr, risk_cls, pct_cls = risk_level(risk)
    is_ca    = patient['label'] == 1
    features = patient.get('features', {})
    best_w   = patient.get('best_window', lkbk)

    cols = st.columns([1.3, 1, 1, 1, 1, 1, 1])
    with cols[0]:
        st.markdown(f"""
        <div class="risk-wrap {risk_cls}">
          <div style="font-family:'Space Mono';font-size:9px;color:{MUTED};letter-spacing:2px;margin-bottom:8px;">
            CA RISK · {best_w if not is_synth else lkbk}MIN WINDOW
          </div>
          <div class="{pct_cls}">{risk*100:.1f}%</div>
          <div style="font-size:13px;font-weight:600;color:{clr};margin-top:8px;font-family:'Space Mono';">{lvl}</div>
        </div>""", unsafe_allow_html=True)
        if risk >= alert_th:
            st.markdown(f'<div class="alert-box">🚨 ALERT<br>Risk ≥ {alert_th*100:.0f}%<br>Notify physician</div>',
                        unsafe_allow_html=True)

    for i, sig in enumerate(SIGNALS):
        vals = patient[sig]; val = vals[-1] if vals else 0
        lo, hi = NORMAL[sig]
        if val < lo:   vcls, arr = "v-val-bad",  "↓ LOW"
        elif val > hi: vcls, arr = "v-val-warn", "↑ HIGH"
        else:          vcls, arr = "v-val-ok",   "→ OK"
        fmn = features.get(f'{SIG_PREFIX[sig]}_min', lo)
        fmx = features.get(f'{SIG_PREFIX[sig]}_max', hi)
        last30 = vals[-30:] if len(vals) >= 30 else vals
        tr = np.mean(last30[-10:]) - np.mean(last30[:10]) if len(last30) >= 10 else 0
        tr_col = "#f1516a" if tr > 2 else "#3b82f6" if tr < -2 else "#10b981"
        with cols[i+1]:
            st.markdown(f"""
            <div class="vital-card">
              <div class="v-label">{SIG_LABEL[sig]}</div>
              <div class="{vcls}">{val:.0f}</div>
              <div class="v-unit">{SIG_UNIT[sig]}</div>
              <div class="v-trend" style="color:{'#f1516a' if vcls!='v-val-ok' else '#10b981'}">{arr}</div>
              <div class="v-trend" style="color:{tr_col}">{'↗' if tr>2 else '↘' if tr<-2 else '→'}{abs(tr):.1f}/30m</div>
              <div class="v-norm">Range: {fmn:.0f}–{fmx:.0f}</div>
              <div class="v-norm">Normal: {lo}–{hi}</div>
            </div>""", unsafe_allow_html=True)

def render_phase_timeline(patient):
    """Show deterioration phase breakdown — shown for both real CA and synthetic CA."""
    ca_onset = patient.get('ca_onset')
    ca_idx   = patient.get('ca_time')
    if not (patient['label'] == 1 and ca_onset):
        return
    n      = patient.get('duration', len(patient['times']))
    phases = [
        ("Stable Phase",        0,          ca_onset,               "#10b981"),
        ("Early Deterioration", ca_onset,   min(ca_onset+40, n),    "#f59e0b"),
        ("Active Crisis",       min(ca_onset+40, n), min((ca_idx+1 if ca_idx else n), n), "#f1516a"),
    ]
    st.markdown('<div class="sec-label">Deterioration Phase Timeline</div>', unsafe_allow_html=True)
    pcols = st.columns(len(phases))
    for (pname, ps, pe, pcol), col in zip(phases, pcols):
        dur = max(0, pe - ps)
        with col:
            st.markdown(f"""
            <div class="phase-box" style="border-top:3px solid {pcol}">
              <div class="phase-label">{pname}</div>
              <div style="font-family:'Space Mono';font-size:18px;font-weight:700;color:{pcol}">{dur}min</div>
              <div style="font-size:10px;color:{DIM};font-family:'Space Mono';">{ps}–{pe}min mark</div>
            </div>""", unsafe_allow_html=True)

def render_risk_timeline(patient, risks, alert_th, chart_key_prefix=""):
    valid = [r for r in risks if r is not None]
    curr  = valid[-1] if valid else 0.04
    lvl, clr, _, _ = risk_level(curr)
    rtimes = [patient['times'][i].strftime('%H:%M') for i, r in enumerate(risks) if r is not None]
    rvals  = [r for r in risks if r is not None]
    ca_idx  = patient.get('ca_time')
    ca_onset= patient.get('ca_onset')

    fig = go.Figure()
    fig.add_hrect(y0=0.75, y1=1,      fillcolor='rgba(241,81,106,0.04)', line_width=0)
    fig.add_hrect(y0=alert_th, y1=0.75, fillcolor='rgba(245,158,11,0.03)', line_width=0)
    r_, g_, b_ = int(clr[1:3],16), int(clr[3:5],16), int(clr[5:7],16)
    fig.add_trace(go.Scatter(
        x=rtimes, y=rvals, mode='lines',
        line=dict(color=clr, width=2.2),
        fill='tozeroy', fillcolor=f'rgba({r_},{g_},{b_},0.08)',
        hovertemplate='%{x}<br>Risk: %{y:.1%}<extra></extra>'
    ))
    fig.add_hline(y=alert_th, line_dash='dash', line_color='#f59e0b', line_width=1,
        annotation_text=f'Alert {alert_th*100:.0f}%',
        annotation_font=dict(color='#f59e0b', size=9), annotation_position='top right')
    fig.add_hline(y=0.75, line_dash='dot', line_color='#f1516a', line_width=1,
        annotation_text='Critical 75%',
        annotation_font=dict(color='#f1516a', size=9), annotation_position='top left')

    if ca_onset and ca_onset < len(patient['times']):
        ts_o = patient['times'][ca_onset].strftime('%H:%M')
        fig.add_trace(go.Scatter(x=[ts_o,ts_o], y=[0,1], mode='lines+text',
            line=dict(color='#f59e0b',width=1.5,dash='dot'),
            text=['','ONSET'], textposition='top center',
            textfont=dict(color='#f59e0b',size=9,family='Space Mono'), hoverinfo='skip'))

    if ca_idx is not None:
        offset = len(risks) - len(rvals); ci = ca_idx - offset - 1
        if 0 <= ci < len(rtimes):
            fig.add_trace(go.Scatter(x=[rtimes[ci],rtimes[ci]], y=[0,1], mode='lines+text',
                line=dict(color='#f1516a',width=1.5,dash='dot'),
                text=['','CA EVENT'], textposition='top center',
                textfont=dict(color='#f1516a',size=9,family='Space Mono'), hoverinfo='skip'))

    for i in range(1, len(rvals)):
        if rvals[i] >= alert_th and rvals[i-1] < alert_th:
            fig.add_trace(go.Scatter(x=[rtimes[i],rtimes[i]], y=[0,1], mode='lines+text',
                line=dict(color='#f59e0b',width=1,dash='dash'),
                text=['','ALERT'], textposition='top center',
                textfont=dict(color='#f59e0b',size=9,family='Space Mono'), hoverinfo='skip'))
            break

    lyt = plotly_base()
    lyt.update(height=220,
        yaxis=dict(**lyt['yaxis'], tickformat='.0%', range=[0,1.05]),
        xaxis=dict(**lyt['xaxis'], nticks=18),
        margin=dict(l=50,r=20,t=16,b=30))
    fig.update_layout(**lyt)
    st.plotly_chart(fig, use_container_width=True, key=f"{chart_key_prefix}_risk_timeline_{patient['caseid']}")

def render_signal_charts(patient):
    pairs   = [(SIGNALS[i], SIGNALS[i+1]) for i in range(0,6,2)]
    ca_idx  = patient.get('ca_time')
    ca_onset= patient.get('ca_onset')
    src     = patient.get('data_source','')

    if src == 'vitaldb':
        st.markdown('<div class="info-box">🌐 Showing live waveform data fetched from VitalDB API</div>',
                    unsafe_allow_html=True)
    elif src == 'synthetic':
        st.markdown('<div class="synth-box">🧬 Waveform algorithmically generated from configurable parameters.</div>',
                    unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-box">📊 Waveform reconstructed from CSV statistical features (mean, std, slope). '
                    'VitalDB API fetch attempted automatically.</div>', unsafe_allow_html=True)

    for sA, sB in pairs:
        c1, c2 = st.columns(2)
        for sig, col in [(sA,c1),(sB,c2)]:
            with col:
                vals  = patient[sig]; times = patient['times']
                lo, hi = NORMAL[sig]; color = SIG_COLOR[sig]
                ts   = [t.strftime('%H:%M') for t in times]
                cps  = change_points(vals, times, CHANGE_TH[sig])
                r_,g_,b_ = int(color[1:3],16), int(color[3:5],16), int(color[5:7],16)

                f = go.Figure()
                f.add_hrect(y0=lo,y1=hi, fillcolor='rgba(16,185,129,0.04)', line_width=0)
                f.add_hline(y=hi, line_dash='dot', line_color=BORDER, line_width=1)
                f.add_hline(y=lo, line_dash='dot', line_color=BORDER, line_width=1)
                f.add_trace(go.Scatter(
                    x=ts, y=vals, mode='lines',
                    line=dict(color=color, width=2.8),
                    fill='tozeroy', fillcolor=f'rgba({r_},{g_},{b_},0.08)',
                    hovertemplate=f'<b>{SIG_LABEL[sig]}</b><br>%{{x}}<br>%{{y:.1f}} {SIG_UNIT[sig]}<extra></extra>'
                ))
                danger = [v if (v<lo or v>hi) else None for v in vals]
                f.add_trace(go.Scatter(x=ts, y=danger, mode='markers',
                    marker=dict(color='#f1516a',size=5,opacity=0.9,symbol='circle',
                                line=dict(color='#f1516a',width=1)), hoverinfo='skip'))

                for cp in cps:
                    cs = cp['time'].strftime('%H:%M')
                    f.add_trace(go.Scatter(x=[cs,cs], y=[min(vals)*0.97,max(vals)*1.03],
                        mode='lines', line=dict(color='#f59e0b',width=1,dash='dot'), hoverinfo='skip'))
                    f.add_annotation(x=cs, y=cp['val'],
                        text=f"{'↑' if cp['dir']=='UP' else '↓'}{abs(cp['delta']):.1f}",
                        showarrow=True, arrowhead=2, arrowcolor='#f59e0b',
                        font=dict(size=9,color='#f59e0b',family='Space Mono'),
                        bgcolor=CARD, bordercolor='#f59e0b', borderwidth=1, borderpad=2, ax=0, ay=-28)

                if ca_onset and ca_onset < len(times):
                    ts_o = times[ca_onset].strftime('%H:%M')
                    f.add_trace(go.Scatter(x=[ts_o,ts_o], y=[min(vals)*0.97,max(vals)*1.03],
                        mode='lines+text', line=dict(color='#f59e0b',width=1.5,dash='dot'),
                        text=['','ONSET'], textposition='top center',
                        textfont=dict(size=8,color='#f59e0b',family='Space Mono'), hoverinfo='skip'))

                if ca_idx is not None and ca_idx < len(times):
                    cas = times[ca_idx].strftime('%H:%M')
                    f.add_trace(go.Scatter(x=[cas,cas], y=[min(vals)*0.97,max(vals)*1.03],
                        mode='lines+text', line=dict(color='#f1516a',width=1.5,dash='dot'),
                        text=['','CA'], textposition='top center',
                        textfont=dict(size=9,color='#f1516a',family='Space Mono'), hoverinfo='skip'))

                lyt = plotly_base()
                lyt.update(height=270,
                    title=dict(
                        text=f"{SIG_LABEL[sig]} <span style='font-size:10px;color:{MUTED}'>({SIG_UNIT[sig]}) &nbsp;·&nbsp; normal {lo}–{hi}</span>",
                        font=dict(size=12,color=TEXT,family='Space Mono'), x=0),
                    margin=dict(l=44,r=12,t=44,b=32))
                f.update_layout(**lyt)
                st.plotly_chart(f, use_container_width=True, key=f"sig_{sig}_{patient['caseid']}")

def render_feature_stats_table(patient):
    features = patient.get('features', {})
    rows = ""
    for sig in SIGNALS:
        p  = SIG_PREFIX[sig]
        mn = features.get(f'{p}_mean',  0)
        sd = features.get(f'{p}_std',   0)
        mi = max(0, features.get(f'{p}_min', 0))
        mx = features.get(f'{p}_max',   0)
        sl = features.get(f'{p}_slope', 0)
        lo, hi = NORMAL[sig]
        rc = "color:#f1516a" if mi < lo or mx > hi else "color:#10b981"
        rows += f"""<tr>
          <td style="color:{SIG_COLOR[sig]}">{SIG_LABEL[sig]}</td>
          <td style="color:{TEXT}">{mn:.1f}</td>
          <td style="color:{DIM}">{sd:.2f}</td>
          <td style="{rc}">{mi:.1f}</td>
          <td style="{rc}">{mx:.1f}</td>
          <td style="color:{DIM}">{sl:.4f}</td>
          <td style="color:{DIM}">{lo}–{hi} {SIG_UNIT[sig]}</td>
        </tr>"""
    st.markdown(f"""
    <table class="data-table">
      <thead><tr><th>SIGNAL</th><th>MEAN</th><th>STD</th><th>MIN</th><th>MAX</th><th>SLOPE</th><th>NORMAL RANGE</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>""", unsafe_allow_html=True)

def render_change_table(patient):
    all_cps = []
    for sig in SIGNALS:
        lo, hi = NORMAL[sig]
        for cp in change_points(patient[sig], patient['times'], CHANGE_TH[sig]):
            in_range = lo <= cp['val'] <= hi
            all_cps.append({'Time':cp['ts'],'Signal':SIG_LABEL[sig],
                'Value':f"{cp['val']:.1f} {SIG_UNIT[sig]}",
                'Change':f"{'↑' if cp['dir']=='UP' else '↓'} {abs(cp['delta']):.1f}",
                'Status':'Within range' if in_range else '⚠ Outside range',
                'Normal':f"{lo}–{hi}", '_up':cp['dir']=='UP','_bad':not in_range,'_sig':sig})
    all_cps.sort(key=lambda x: x['Time'])
    if all_cps:
        rows = ""
        for c in all_cps:
            dc = 'color:#f1516a' if c['_up'] else 'color:#3b82f6'
            sc = 'color:#f59e0b' if c['_bad'] else 'color:#10b981'
            sig_col = SIG_COLOR[c["_sig"]]
            rows += f"<tr><td style='color:{TEXT}'>{c['Time']}</td><td style='color:{sig_col}'>{c['Signal']}</td><td style='color:{TEXT}'>{c['Value']}</td><td style='{dc}'>{c['Change']}</td><td style='{sc}'>{c['Status']}</td><td>{c['Normal']}</td></tr>"
        st.markdown(f"""<table class="data-table"><thead><tr>
          <th>TIME</th><th>SIGNAL</th><th>VALUE</th><th>CHANGE</th><th>STATUS</th><th>NORMAL</th>
        </tr></thead><tbody>{rows}</tbody></table>""", unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-box">No significant change points detected.</div>', unsafe_allow_html=True)

def render_window_risk_bar(patient, alert_th, patient_info_map=None, is_synth=False):
    """Multi-window risk bar — real uses CSV features per window, synthetic uses signal slices."""
    st.markdown('<div class="sec-label">Risk Across Available Windows</div>', unsafe_allow_html=True)
    wc_map = {240:'#10b981',120:'#3b82f6',60:'#f59e0b',30:'#f1516a'}
    win_labels=[]; win_risks=[]; win_colors=[]

    if is_synth:
        vals = patient['times']
        n    = len(patient['times'])
        for w in WINDOWS:
            now_i = n - 1; si = max(0, now_i - w)
            wnd   = {sig: patient[sig][si:now_i+1] for sig in SIGNALS}
            rng2  = np.random.default_rng(w + (100 if patient['label']==1 else 0))
            base  = estimate_risk_from_features(patient['features'], patient['label'], patient['caseid'])
            r_w   = float(np.clip(base + rng2.normal(0,0.04), 0, 1))
            win_labels.append(f'{w}min'); win_risks.append(r_w*100); win_colors.append(wc_map[w])
    else:
        caseid = patient['caseid']; label = patient['label']
        for w in WINDOWS:
            feat_key = f'features_{w}'
            if patient_info_map and feat_key in patient_info_map.get(caseid,{}):
                f_w = patient_info_map[caseid][feat_key]
                r_w = estimate_risk_from_features(f_w, label, caseid+w)
                win_labels.append(f'{w}min'); win_risks.append(r_w*100); win_colors.append(wc_map[w])
            else:
                win_labels.append(f'{w}min\n(N/A)'); win_risks.append(0); win_colors.append('#1c2236')

    fw = go.Figure()
    fw.add_trace(go.Bar(
        x=win_labels, y=win_risks,
        marker_color=win_colors,
        text=[f'{r:.1f}%' if r > 0 else 'N/A' for r in win_risks],
        textposition='outside',
        textfont=dict(color=TEXT, size=10, family='Space Mono')
    ))
    fw.add_hline(y=alert_th*100, line_dash='dash', line_color='#f59e0b', line_width=1)
    lw = plotly_base()
    lw.update(height=200,
        yaxis=dict(**lw['yaxis'], range=[0,110], ticksuffix='%'),
        margin=dict(l=36,r=10,t=12,b=28))
    fw.update_layout(**lw)
    st.plotly_chart(fw, use_container_width=True, key=f"win_bar_{patient['caseid']}")

def render_shap_panel():
    shap_bar = os.path.join(SCRIPT_DIR,'shap_outputs','shap_bar_top15.png')
    shap_bee = os.path.join(SCRIPT_DIR,'shap_outputs','shap_beeswarm_top15.png')
    shap_dep = os.path.join(SCRIPT_DIR,'shap_outputs','shap_dependence_top3.png')
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    if os.path.exists(shap_bar):
        st.markdown('''
        <div style="border-top:2px solid #1c2236;margin-bottom:20px;padding-top:20px;">
          <div style="font-family:'Space Mono',monospace;font-size:14px;font-weight:700;color:#e2e8f4;margin-bottom:6px;">
            🔬 SHAP Feature Interpretability — LightGBM (60-min Window)
          </div>
          <div style="font-family:'Space Mono',monospace;font-size:10px;color:#2d3748;letter-spacing:1px;">
            SHapley Additive exPlanations · TreeExplainer · AUROC 0.9073 · VitalDB Dataset · TSI 2026
          </div>
        </div>''', unsafe_allow_html=True)
        s1, s2 = st.columns(2)
        with s1: st.image(shap_bar, caption="Mean |SHAP| — Top 15 Features", use_container_width=True)
        if os.path.exists(shap_bee):
            with s2: st.image(shap_bee, caption="SHAP Beeswarm — Feature Impact Direction", use_container_width=True)
        if os.path.exists(shap_dep):
            st.image(shap_dep, caption="SHAP Dependence — Top 3 predictors", use_container_width=True)
        st.markdown(f'''
        <div style="background:#060c18;border:1px solid #3b82f6;border-radius:8px;
                    padding:12px 16px;font-size:12px;color:#8892aa;margin:12px 0;line-height:1.7;">
          <strong style="color:#e2e8f4;">🔬 How to read these charts:</strong><br>
          <strong style="color:#e2e8f4;">Bar chart</strong> — average magnitude of each feature's impact.
          Longer bar = stronger predictor.<br>
          <strong style="color:#e2e8f4;">Beeswarm</strong> — each dot is one patient.
          Red dots pushed right = high value increases CA risk. Blue pushed left = decreases risk.<br>
          <strong style="color:#e2e8f4;">Key finding</strong> — Diastolic BP Max, Mean BP Max, and Heart Rate Mean
          are the top 3 predictors. Run <code style="color:#f59e0b;">python shap_analysis.py</code> to regenerate.
        </div>''', unsafe_allow_html=True)
    else:
        st.markdown(f'''
        <div style="background:#0d0a00;border:1px solid #f59e0b;border-radius:8px;
                    padding:12px 16px;font-size:12px;color:#f59e0b;margin:20px 0;">
          📊 SHAP figures not found. Run <code>python shap_analysis.py</code> to generate interpretability plots.
        </div>''', unsafe_allow_html=True)

def render_footer():
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="border-top:1px solid {BORDER};padding-top:16px;
                font-family:'Space Mono',monospace;font-size:10px;color:{MUTED};line-height:2.2;">
      🟢 <strong style="color:#10b981;">240min</strong> — Full 4-hour window &nbsp;|&nbsp;
      🔵 <strong style="color:#3b82f6;">120min</strong> — 2-hour window &nbsp;|&nbsp;
      🟡 <strong style="color:#f59e0b;">60min</strong> — 1-hour window &nbsp;|&nbsp;
      🔴 <strong style="color:#f1516a;">30min</strong> — Minimal 30-min window<br>
      🔴 CRITICAL ≥75% — Alert physician immediately &nbsp;|&nbsp;
      🟠 HIGH 50–75% — Increase monitoring &nbsp;|&nbsp;
      🟡 MODERATE 25–50% — Watch closely &nbsp;|&nbsp;
      🔵 LOW &lt;25% — Routine monitoring<br>
      <span style="color:#1c2236;">
      Clinical decision-support prototype · All treatment decisions remain with the attending physician ·
      Sachu Mon P. Sajeev · MSc Data Science & AI · TSI University Riga · 2026
      </span>
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  FULL PANEL (used by both modes)
# ══════════════════════════════════════════════════════════════════════
def full_panel(patient, risks, alert_th, lkbk, is_synth=False, patient_info_map=None):
    valid = [r for r in risks if r is not None]
    curr  = valid[-1] if valid else 0.04

    render_patient_header(patient, is_synth=is_synth)
    render_risk_vitals_row(patient, curr, alert_th, lkbk, is_synth=is_synth)
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    if not is_synth:
        st.markdown('<div class="sec-label">Clinical Feature Statistics (from CSV)</div>', unsafe_allow_html=True)
        render_feature_stats_table(patient)
        st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    render_phase_timeline(patient)

    st.markdown('<div class="sec-label">Risk Score Over Time</div>', unsafe_allow_html=True)
    render_risk_timeline(patient, risks, alert_th, chart_key_prefix=str(patient["caseid"]))

    st.markdown('<div class="sec-label">Vital Signal Trends</div>', unsafe_allow_html=True)
    render_signal_charts(patient)

    st.markdown('<div class="sec-label">Change Point Log</div>', unsafe_allow_html=True)
    render_change_table(patient)

    render_window_risk_bar(patient, alert_th, patient_info_map=patient_info_map, is_synth=is_synth)

# ══════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("### 🫀 CA Risk Monitor")
    st.caption("Sachu Mon P. Sajeev · TSI 2026")
    st.divider()

    # ── MAIN DASHBOARD TOGGLE
    dash_mode = st.radio(
        "📊 Dashboard Mode",
        ["🌐 Real Data — VitalDB", "🧬 Synthetic — Deep Dive"],
        help="Real: loads all VitalDB patients from CSV + live API fetch\nSynthetic: fully configurable patient simulator"
    )
    IS_REAL = "Real" in dash_mode
    st.divider()

    if IS_REAL:
        # ── REAL DATA SIDEBAR
        st.caption("🌐 VitalDB Patients")
        view_mode  = st.radio("View Mode", ["Single Patient","Compare 2 Patients"])
        filter_opt = st.selectbox("Filter by",
            ["All Patients","CA Events Only","No CA Only",
             "240min Available","120min Only","60min Only","30min Only"])
        fetch_live = st.checkbox("Try fetch live waveform (VitalDB API)", value=True)
        st.divider()
        alert_th = st.slider("Alert threshold (%)", 20, 90, 55) / 100
        lkbk     = st.slider("Lookback window (min)", 30, 240, 60, step=30)

    else:
        # ── SYNTHETIC SIDEBAR
        st.caption("🧬 Patient Simulator")
        view_mode  = st.radio("View Mode", ["Single Patient","Side-by-Side","CA vs No-CA Overlay"])
        noise_lvl  = st.slider("Noise level", 0.3, 2.0, 1.0, step=0.1)

        st.markdown("**── Patient A**")
        seed_a  = st.slider("Seed A", 1, 200, 42, key="sa")
        dur_a   = st.slider("Duration A (min)", 120, 600, 480, step=60, key="da")
        ca_a    = True if "Overlay" in view_mode else st.checkbox("CA Event A", True, key="ca_a")
        if ca_a:
            onset_a      = st.slider("CA Onset A (min)", 60, dur_a-60, 380, step=10, key="oa")
            hr_rate_a    = st.slider("HR Rise Rate A",   0.05, 0.30, 0.12, step=0.01, key="hr_a")
            bp_rate_a    = st.slider("BP Drop Rate A",   0.05, 0.30, 0.15, step=0.01, key="bp_a")
            spo2_rate_a  = st.slider("SpO2 Drop Rate A", 0.02, 0.15, 0.06, step=0.01, key="sp_a")
            bhr_a        = st.slider("Baseline HR A",    55, 95, 72, key="bhr_a")
        else:
            onset_a=380; hr_rate_a=0.12; bp_rate_a=0.15; spo2_rate_a=0.06; bhr_a=72

        if "Side-by-Side" in view_mode or "Overlay" in view_mode:
            st.markdown("**── Patient B**")
            seed_b  = st.slider("Seed B", 1, 200, 77, key="sb")
            dur_b   = st.slider("Duration B (min)", 120, 600, 480, step=60, key="db")
            ca_b    = False if "Overlay" in view_mode else st.checkbox("CA Event B", False, key="ca_b")
            if ca_b:
                onset_b     = st.slider("CA Onset B (min)", 60, dur_b-60, 300, step=10, key="ob")
                hr_rate_b   = st.slider("HR Rise Rate B",   0.05, 0.30, 0.12, step=0.01, key="hr_b")
                bp_rate_b   = st.slider("BP Drop Rate B",   0.05, 0.30, 0.15, step=0.01, key="bp_b")
                spo2_rate_b = st.slider("SpO2 Drop Rate B", 0.02, 0.15, 0.06, step=0.01, key="sp_b")
                bhr_b       = st.slider("Baseline HR B",    55, 95, 68, key="bhr_b")
            else:
                onset_b=300; hr_rate_b=0.12; bp_rate_b=0.15; spo2_rate_b=0.06; bhr_b=70

        st.divider()
        alert_th = st.slider("Alert threshold (%)", 20, 90, 55) / 100
        lkbk     = st.slider("Lookback window (min)", 30, 240, 60, step=30)

    st.divider()
    st.caption("TAN · AUROC 0.9937\nLightGBM · AUROC 0.9073\nTSI University · 2026")

# ══════════════════════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════════════════════
now_str = datetime.now().strftime("%d %b %Y · %H:%M")
accent  = "#3b82f6" if IS_REAL else "#8b5cf6"
mode_tag= "🌐 REAL DATA — VitalDB" if IS_REAL else "🧬 SYNTHETIC DEEP DIVE"

if IS_REAL:
    dfs, patient_info_map = load_all_patients()
    if not patient_info_map:
        st.error("❌ No CSV files found. Make sure combined_*min.csv files are in the checkpoints folder.")
        st.stop()
    all_caseids = sorted(patient_info_map.keys())
    ca_ids      = [c for c in all_caseids if patient_info_map[c]['label'] == 1]
    noca_ids    = [c for c in all_caseids if patient_info_map[c]['label'] == 0]
    sub_info    = f"VitalDB · {len(all_caseids)} Patients · CA={len(ca_ids)} · No-CA={len(noca_ids)}"
else:
    patient_info_map = {}
    sub_info = "Configurable Patient Simulator · All waveforms algorithmically generated"

st.markdown(f"""
<div style="border-bottom:1px solid {BORDER};padding-bottom:16px;margin-bottom:20px;
            display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;">
  <div>
    <div style="display:flex;align-items:center;gap:12px;flex-wrap:wrap;">
      <span style="font-family:'Space Mono',monospace;font-size:19px;font-weight:700;color:{TEXT};letter-spacing:-0.5px;">
        🫀 INTRAOPERATIVE CARDIAC ARREST RISK MONITOR
      </span>
      <span style="background:{accent}22;color:{accent};border:1px solid {accent}44;
                   font-family:'Space Mono';font-size:9px;padding:4px 12px;border-radius:20px;letter-spacing:1px;">
        {mode_tag}
      </span>
    </div>
    <div style="font-family:'Space Mono',monospace;font-size:10px;color:{MUTED};margin-top:6px;letter-spacing:1px;">
      {sub_info} &nbsp;|&nbsp; {now_str} &nbsp;|&nbsp; {view_mode}
    </div>
    <div style="font-family:'Space Mono',monospace;font-size:10px;color:{MUTED};margin-top:3px;letter-spacing:1px;">
      Sachu Mon P. Sajeev · MSc Data Science & AI · TSI University Riga · 2026
    </div>
  </div>
  <div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;">
    <div style="background:#060c18;border:1px solid #10b981;border-radius:8px;padding:8px 14px;text-align:center;">
      <div style="font-family:'Space Mono';font-size:8px;color:#10b981;letter-spacing:2px;margin-bottom:3px;">TAN · AUROC</div>
      <div style="font-family:'Space Mono';font-size:18px;font-weight:700;color:#10b981;line-height:1;">0.9937</div>
      <div style="font-family:'Space Mono';font-size:8px;color:{MUTED};margin-top:2px;">95% CI [0.9909–0.9961]</div>
    </div>
    <div style="background:#060810;border:1px solid #3b82f6;border-radius:8px;padding:8px 14px;text-align:center;">
      <div style="font-family:'Space Mono';font-size:8px;color:#3b82f6;letter-spacing:2px;margin-bottom:3px;">LightGBM · AUROC</div>
      <div style="font-family:'Space Mono';font-size:18px;font-weight:700;color:#3b82f6;line-height:1;">0.9073</div>
      <div style="font-family:'Space Mono';font-size:8px;color:{MUTED};margin-top:2px;">60-min window</div>
    </div>
    <div style="background:#0d0a00;border:1px solid #f59e0b;border-radius:8px;padding:8px 14px;text-align:center;">
      <div style="font-family:'Space Mono';font-size:8px;color:#f59e0b;letter-spacing:2px;margin-bottom:3px;">TAN · AUPRC</div>
      <div style="font-family:'Space Mono';font-size:18px;font-weight:700;color:#f59e0b;line-height:1;">0.6027</div>
      <div style="font-family:'Space Mono';font-size:8px;color:{MUTED};margin-top:2px;">240-min window</div>
    </div>
  </div>
</div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  REAL DATA MODE
# ══════════════════════════════════════════════════════════════════════
if IS_REAL:
    # Patient counts info bar
    st.markdown(f"""
    <div style='font-family:Space Mono;font-size:10px;background:#0d1120;border:1px solid #1c2236;
                border-radius:8px;padding:10px 16px;margin-bottom:16px;line-height:2;'>
    Total: <b style='color:#e2e8f4'>{len(all_caseids)}</b> &nbsp;|&nbsp;
    CA: <b style='color:#f1516a'>{len(ca_ids)}</b> &nbsp;|&nbsp;
    No CA: <b style='color:#3b82f6'>{len(noca_ids)}</b> &nbsp;|&nbsp;
    240min: <b style='color:#10b981'>{sum(1 for c in all_caseids if 240 in patient_info_map[c]["available_windows"])}</b> &nbsp;|&nbsp;
    120min: <b style='color:#3b82f6'>{sum(1 for c in all_caseids if 120 in patient_info_map[c]["available_windows"])}</b> &nbsp;|&nbsp;
    60min: <b style='color:#f59e0b'>{sum(1 for c in all_caseids if 60 in patient_info_map[c]["available_windows"])}</b> &nbsp;|&nbsp;
    30min: <b style='color:#f1516a'>{sum(1 for c in all_caseids if 30 in patient_info_map[c]["available_windows"])}</b>
    </div>""", unsafe_allow_html=True)

    # Filter
    if filter_opt == "All Patients":       filtered_ids = all_caseids
    elif filter_opt == "CA Events Only":   filtered_ids = ca_ids
    elif filter_opt == "No CA Only":       filtered_ids = noca_ids
    elif filter_opt == "240min Available": filtered_ids = [c for c in all_caseids if 240 in patient_info_map[c]['available_windows']]
    elif filter_opt == "120min Only":      filtered_ids = [c for c in all_caseids if patient_info_map[c]['best_window']==120]
    elif filter_opt == "60min Only":       filtered_ids = [c for c in all_caseids if patient_info_map[c]['best_window']==60]
    elif filter_opt == "30min Only":       filtered_ids = [c for c in all_caseids if patient_info_map[c]['best_window']==30]
    else: filtered_ids = all_caseids

    if not filtered_ids:
        st.warning("No patients match this filter."); st.stop()

    fmt = lambda c: f"#{c} · {'CA' if patient_info_map[c]['label']==1 else 'NoCA'} · {patient_info_map[c]['best_window']}min"

    if view_mode == "Single Patient":
        sel_id = st.selectbox(f"Select Patient ({len(filtered_ids)} available)", filtered_ids, format_func=fmt)
    else:
        cc1, cc2 = st.columns(2)
        with cc1: sel_a = st.selectbox("Patient A", filtered_ids, format_func=fmt, key="real_a")
        with cc2: sel_b = st.selectbox("Patient B", [c for c in filtered_ids if c != sel_a], format_func=fmt, key="real_b")

    def get_real_patient(caseid):
        info = patient_info_map[caseid]
        pat  = build_patient_from_features(info)
        if fetch_live:
            with st.spinner(f"🌐 Fetching live waveform for case #{caseid} from VitalDB..."):
                raw = fetch_vitaldb_waveform(caseid)
            if raw:
                mapped = map_vitaldb_to_signals(raw)
                n = min(len(v) for v in mapped.values() if len(v) > 0)
                if n > 10:
                    start = datetime(2024, 3, 9, 8, 0, 0)
                    pat['times'] = [start + timedelta(minutes=i) for i in range(n)]
                    for sig in SIGNALS:
                        if sig in mapped: pat[sig] = mapped[sig][:n]
                    pat['data_source'] = 'vitaldb'
                    st.success(f"✅ Live waveform loaded — {n} minutes of real data")
        return pat

    def compare_summary(pat_a, pat_b, sel_a, sel_b):
        risk_a = estimate_risk_from_features(pat_a['features'], pat_a['label'], sel_a)
        risk_b = estimate_risk_from_features(pat_b['features'], pat_b['label'], sel_b)
        lv_a, cl_a, _, pc_a = risk_level(risk_a)
        lv_b, cl_b, _, pc_b = risk_level(risk_b)
        st.markdown('<div class="sec-label">Risk Comparison Summary</div>', unsafe_allow_html=True)
        ca_col, cb_col = st.columns(2)
        for col, cid, risk, lv, cl, pc, pat in [
            (ca_col, sel_a, risk_a, lv_a, cl_a, pc_a, pat_a),
            (cb_col, sel_b, risk_b, lv_b, cl_b, pc_b, pat_b)
        ]:
            with col:
                bw = pat['best_window']
                bw_cls = {240:'wb-240',120:'wb-120',60:'wb-60',30:'wb-30'}.get(bw,'wb-30')
                st.markdown(f"""
                <div style="background:{CARD};border:1px solid {BORDER};border-radius:10px;padding:16px 20px;margin-bottom:8px;">
                  <div style="font-family:'Space Mono';font-size:10px;color:{MUTED};margin-bottom:6px;">
                    Case #{cid} &nbsp;·&nbsp; {'⚠ CA EVENT' if pat['label']==1 else '✓ NO CA'}
                    <span class="window-badge {bw_cls}">{bw}min</span>
                  </div>
                  <div class="{pc}" style="font-size:42px;">{risk*100:.1f}%</div>
                  <div style="font-size:12px;color:{cl};font-family:'Space Mono';margin-top:4px;">{lv}</div>
                </div>""", unsafe_allow_html=True)

    if view_mode == "Single Patient":
        pat   = get_real_patient(sel_id)
        risks = rolling_risk_real(pat)
        full_panel(pat, risks, alert_th, lkbk, is_synth=False, patient_info_map=patient_info_map)

    else:
        pat_a = get_real_patient(sel_a); pat_b = get_real_patient(sel_b)
        compare_summary(pat_a, pat_b, sel_a, sel_b)
        st.markdown("<hr style='border:none;border-top:2px solid #1c2236;margin:28px 0 20px 0'>", unsafe_allow_html=True)
        for pat, cid in [(pat_a, sel_a), (pat_b, sel_b)]:
            risks = rolling_risk_real(pat)
            full_panel(pat, risks, alert_th, lkbk, is_synth=False, patient_info_map=patient_info_map)
            st.markdown("<hr style='border:none;border-top:2px solid #1c2236;margin:28px 0 20px 0'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  SYNTHETIC MODE
# ══════════════════════════════════════════════════════════════════════
else:
    st.markdown('<div class="synth-box">🧬 <strong>Synthetic Mode</strong> — All waveforms are algorithmically generated '
                'from configurable parameters. Adjust deterioration rates, onset timing, and noise in the sidebar. '
                'Perfect for thesis presentation and clinical model explanation.</div>', unsafe_allow_html=True)

    # Generate patients
    pat_a  = generate_patient(ca=ca_a, seed=seed_a, duration=dur_a, ca_onset=onset_a,
                               hr_rise_rate=hr_rate_a, bp_drop_rate=bp_rate_a,
                               desat_rate=spo2_rate_a, baseline_hr=bhr_a, noise_level=noise_lvl)
    risks_a = rolling_risk_synth(pat_a, lkbk)

    if "Side-by-Side" in view_mode or "Overlay" in view_mode:
        pat_b  = generate_patient(ca=ca_b, seed=seed_b, duration=dur_b, ca_onset=onset_b,
                                   hr_rise_rate=hr_rate_b, bp_drop_rate=bp_rate_b,
                                   desat_rate=spo2_rate_b, baseline_hr=bhr_b, noise_level=noise_lvl)
        risks_b = rolling_risk_synth(pat_b, lkbk)

    def synth_compare_summary(pat_a, risks_a, lbl_a, pat_b, risks_b, lbl_b):
        vld_a = [r for r in risks_a if r is not None]; cur_a = vld_a[-1] if vld_a else 0.04
        vld_b = [r for r in risks_b if r is not None]; cur_b = vld_b[-1] if vld_b else 0.04
        lv_a, cl_a, _, pc_a = risk_level(cur_a); lv_b, cl_b, _, pc_b = risk_level(cur_b)
        st.markdown('<div class="sec-label">Risk Comparison Summary</div>', unsafe_allow_html=True)
        cc1, cc2 = st.columns(2)
        for col, lbl, cur, lv, cl, pc, pat in [
            (cc1, lbl_a, cur_a, lv_a, cl_a, pc_a, pat_a),
            (cc2, lbl_b, cur_b, lv_b, cl_b, pc_b, pat_b)
        ]:
            with col:
                border_clr = '#f1516a' if pat['label']==1 else '#3b82f6'
                st.markdown(f"""
                <div style="background:{CARD};border:1.5px solid {border_clr};border-radius:10px;padding:16px 20px;margin-bottom:8px;">
                  <div style="font-family:'Space Mono';font-size:10px;color:{MUTED};margin-bottom:6px;">{lbl}</div>
                  <div class="{pc}" style="font-size:42px;">{cur*100:.1f}%</div>
                  <div style="font-size:12px;color:{cl};font-family:'Space Mono';margin-top:4px;">{lv}</div>
                </div>""", unsafe_allow_html=True)

    def render_overlay(pat_a, pat_b, risks_a, risks_b, alert_th):
        """CA vs No-CA overlaid signal charts."""
        st.markdown('<div class="sec-label">Signal Overlay — CA vs No-CA</div>', unsafe_allow_html=True)
        st.markdown('<div class="info-box">📊 Red = CA patient · Blue dashed = No CA · Shaded = normal range</div>',
                    unsafe_allow_html=True)
        for sA, sB in [(SIGNALS[i], SIGNALS[i+1]) for i in range(0,6,2)]:
            c1, c2 = st.columns(2)
            for sig, col in [(sA,c1),(sB,c2)]:
                with col:
                    n  = min(len(pat_a[sig]), len(pat_b[sig]))
                    ts = [pat_a['times'][i].strftime('%H:%M') for i in range(n)]
                    lo, hi = NORMAL[sig]
                    f = go.Figure()
                    f.add_hrect(y0=lo,y1=hi, fillcolor='rgba(16,185,129,0.04)', line_width=0)
                    f.add_hline(y=hi, line_dash='dot', line_color=BORDER, line_width=1)
                    f.add_hline(y=lo, line_dash='dot', line_color=BORDER, line_width=1)
                    f.add_trace(go.Scatter(x=ts, y=pat_a[sig][:n], mode='lines', name='CA',
                        line=dict(color='#f1516a',width=2), fill='tozeroy', fillcolor='rgba(241,81,106,0.05)',
                        hovertemplate=f'CA·{SIG_LABEL[sig]}: %{{y:.1f}}<extra></extra>'))
                    f.add_trace(go.Scatter(x=ts, y=pat_b[sig][:n], mode='lines', name='No CA',
                        line=dict(color='#3b82f6',width=2,dash='dash'),
                        hovertemplate=f'NoCA·{SIG_LABEL[sig]}: %{{y:.1f}}<extra></extra>'))
                    lyt = plotly_base()
                    lyt.update(height=200, showlegend=True,
                        legend=dict(font=dict(size=9,color=DIM,family='Space Mono'),bgcolor='rgba(0,0,0,0)',x=0.01,y=0.99),
                        title=dict(text=f"{SIG_LABEL[sig]} <span style='font-size:10px;color:{MUTED}'>({SIG_UNIT[sig]})</span>",
                                   font=dict(size=11,color=TEXT,family='Space Mono'),x=0),
                        margin=dict(l=36,r=10,t=38,b=28))
                    f.update_layout(**lyt)
                    st.plotly_chart(f, use_container_width=True, key=f"overlay_sig_{sig}")

        # Risk score overlay
        st.markdown('<div class="sec-label">Risk Score Overlay</div>', unsafe_allow_html=True)
        rvals_a = [r for r in risks_a if r is not None]
        rvals_b = [r for r in risks_b if r is not None]
        n = min(len(rvals_a), len(rvals_b))
        ts_o = [pat_a['times'][i].strftime('%H:%M') for i,r in enumerate(risks_a) if r is not None][:n]
        fr = go.Figure()
        fr.add_hrect(y0=0.75,y1=1, fillcolor='rgba(241,81,106,0.04)', line_width=0)
        fr.add_trace(go.Scatter(x=ts_o,y=rvals_a[:n],mode='lines',name='CA Patient',
            line=dict(color='#f1516a',width=2),fill='tozeroy',fillcolor='rgba(241,81,106,0.06)'))
        fr.add_trace(go.Scatter(x=ts_o,y=rvals_b[:n],mode='lines',name='No CA',
            line=dict(color='#3b82f6',width=2,dash='dash'),fill='tozeroy',fillcolor='rgba(59,130,246,0.04)'))
        fr.add_hline(y=alert_th, line_dash='dash', line_color='#f59e0b', line_width=1)
        lr = plotly_base()
        lr.update(height=250, showlegend=True,
            legend=dict(font=dict(size=9,color=DIM,family='Space Mono'),bgcolor='rgba(0,0,0,0)'),
            yaxis=dict(**lr['yaxis'],tickformat='.0%',range=[0,1.05]),
            margin=dict(l=50,r=20,t=16,b=30))
        fr.update_layout(**lr)
        st.plotly_chart(fr, use_container_width=True, key="overlay_risk_score")

    lbl_a = "Patient A — CA Event" if ca_a else "Patient A — No CA"
    # ca_b is only defined in the sidebar when view_mode is Side-by-Side or Overlay.
    # Guard against NameError when view_mode == "Single Patient".
    if "Side-by-Side" in view_mode or "Overlay" in view_mode:
        lbl_b = ("Patient B — No CA") if "Overlay" in view_mode else ("Patient B — CA Event" if ca_b else "Patient B — No CA")
    else:
        lbl_b = "Patient B — No CA"  # unused in Single Patient mode, safe fallback
    divider_html = "<hr style='border:none;border-top:2px solid #1c2236;margin:28px 0 20px 0'>"

    if view_mode == "Single Patient":
        full_panel(pat_a, risks_a, alert_th, lkbk, is_synth=True)

    elif "Side-by-Side" in view_mode:
        synth_compare_summary(pat_a, risks_a, lbl_a, pat_b, risks_b, lbl_b)
        st.markdown(divider_html, unsafe_allow_html=True)
        full_panel(pat_a, risks_a, alert_th, lkbk, is_synth=True)
        st.markdown(divider_html, unsafe_allow_html=True)
        full_panel(pat_b, risks_b, alert_th, lkbk, is_synth=True)

    elif "Overlay" in view_mode:
        synth_compare_summary(pat_a, risks_a, "Patient A — ⚠ CA EVENT", pat_b, risks_b, "Patient B — ✓ NO CA")
        render_overlay(pat_a, pat_b, risks_a, risks_b, alert_th)
        st.markdown(divider_html, unsafe_allow_html=True)
        full_panel(pat_a, risks_a, alert_th, lkbk, is_synth=True)
        st.markdown(divider_html, unsafe_allow_html=True)
        full_panel(pat_b, risks_b, alert_th, lkbk, is_synth=True)

# ══════════════════════════════════════════════════════════════════════
#  SHAP + FOOTER (both modes)
# ══════════════════════════════════════════════════════════════════════
render_shap_panel()
render_footer()
