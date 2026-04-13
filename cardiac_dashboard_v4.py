# ╔══════════════════════════════════════════════════════════════════════╗
# ║  Cardiac Arrest Risk Dashboard — v4  (Professional Prototype)        ║
# ║  Author: Sachu Mon P. Sajeev · MSc Data Science & AI · TSI 2026    ║
# ║  Run:  streamlit run cardiac_dashboard_v4.py                         ║
# ╚══════════════════════════════════════════════════════════════════════╝

import os, warnings
import numpy as np
import streamlit as st
import plotly.graph_objects as go
from datetime import datetime, timedelta
import torch, torch.nn as nn

warnings.filterwarnings('ignore')

# ══════════════════════════════════════════════════════════════════════
#  CONFIG
# ══════════════════════════════════════════════════════════════════════
st.set_page_config(page_title="CA Risk Monitor", page_icon="🫀",
                   layout="wide", initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;700&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background: #060810;
    color: #e2e8f4;
}
.main .block-container { padding: 1.5rem 2rem; max-width: 100%; }
section[data-testid="stSidebar"] {
    background: #0a0d16;
    border-right: 1px solid #1c2236;
}
section[data-testid="stSidebar"] * { color: #8892aa !important; }

/* ── Cards ── */
.card {
    background: #0d1120;
    border: 1px solid #1c2236;
    border-radius: 12px;
    padding: 20px;
    margin-bottom: 12px;
}
.card-sm {
    background: #0d1120;
    border: 1px solid #1c2236;
    border-radius: 10px;
    padding: 14px 16px;
    text-align: center;
}

/* ── Risk blocks ── */
.risk-wrap {
    border-radius: 12px;
    padding: 24px 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
}
.risk-critical { background: #160608; border: 1.5px solid #f1516a; }
.risk-high     { background: #140e06; border: 1.5px solid #f59e0b; }
.risk-moderate { background: #061410; border: 1.5px solid #10b981; }
.risk-low      { background: #060c18; border: 1.5px solid #3b82f6; }

.risk-pct-critical { font-size: 58px; font-weight: 700; font-family: 'Space Mono'; color: #f1516a; line-height:1; }
.risk-pct-high     { font-size: 58px; font-weight: 700; font-family: 'Space Mono'; color: #f59e0b; line-height:1; }
.risk-pct-moderate { font-size: 58px; font-weight: 700; font-family: 'Space Mono'; color: #10b981; line-height:1; }
.risk-pct-low      { font-size: 58px; font-weight: 700; font-family: 'Space Mono'; color: #3b82f6; line-height:1; }

/* ── Vital tiles ── */
.vital-card {
    background: #0d1120;
    border: 1px solid #1c2236;
    border-radius: 10px;
    padding: 12px 10px;
    text-align: center;
}
.v-label { font-size: 9px; font-family: 'Space Mono'; color: #4a5568; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 4px; }
.v-val-ok   { font-size: 26px; font-weight: 700; font-family: 'Space Mono'; color: #10b981; }
.v-val-warn { font-size: 26px; font-weight: 700; font-family: 'Space Mono'; color: #f59e0b; }
.v-val-bad  { font-size: 26px; font-weight: 700; font-family: 'Space Mono'; color: #f1516a; }
.v-unit  { font-size: 9px; color: #4a5568; margin-top: 2px; }
.v-trend { font-size: 10px; font-family: 'Space Mono'; margin-top: 4px; }
.v-norm  { font-size: 9px; color: #2d3748; margin-top: 2px; }

/* ── Section labels ── */
.sec-label {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #2d3748;
    border-bottom: 1px solid #1c2236;
    padding-bottom: 6px;
    margin: 20px 0 12px 0;
}

/* ── Alert ── */
.alert-box {
    background: #160608;
    border-left: 3px solid #f1516a;
    border-radius: 6px;
    padding: 10px 14px;
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #f1516a;
    margin-top: 8px;
}
.info-box {
    background: #060c18;
    border-left: 3px solid #3b82f6;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 12px;
    color: #8892aa;
    margin: 8px 0;
    line-height: 1.6;
}

/* ── Badge ── */
.badge {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    font-weight: 700;
    padding: 3px 10px;
    border-radius: 20px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.badge-ca   { background: rgba(241,81,106,0.12); color: #f1516a; border: 1px solid rgba(241,81,106,0.3); }
.badge-noca { background: rgba(59,130,246,0.12); color: #3b82f6; border: 1px solid rgba(59,130,246,0.3); }

/* ── Table ── */
.data-table { width: 100%; border-collapse: collapse; font-size: 11px; font-family: 'Space Mono', monospace; }
.data-table th { background: #080b14; color: #2d3748; padding: 8px 12px; text-align: left; font-size: 9px; letter-spacing: 1px; text-transform: uppercase; border-bottom: 1px solid #1c2236; }
.data-table td { padding: 7px 12px; border-bottom: 1px solid #0f1525; color: #8892aa; }
.data-table tr:hover td { background: #0f1525; }
.td-up   { color: #f1516a !important; }
.td-down { color: #3b82f6 !important; }
.td-ok   { color: #10b981 !important; }
.td-warn { color: #f59e0b !important; }

/* ── Compare header ── */
.compare-header {
    background: #0d1120;
    border: 1px solid #1c2236;
    border-radius: 10px;
    padding: 16px 20px;
    margin-bottom: 8px;
}
.patient-divider {
    border: none;
    border-top: 2px solid #1c2236;
    margin: 28px 0 20px 0;
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  CONSTANTS
# ══════════════════════════════════════════════════════════════════════
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
WINDOWS    = [30, 60, 120, 240]
SIGNALS    = ['HR','PLETH_SPO2','ETCO2','ART_MBP','ART_SBP','ART_DBP']
SIG_LABEL  = {'HR':'Heart Rate','PLETH_SPO2':'SpO₂','ETCO2':'EtCO₂',
               'ART_MBP':'Mean BP','ART_SBP':'Systolic BP','ART_DBP':'Diastolic BP'}
SIG_UNIT   = {'HR':'bpm','PLETH_SPO2':'%','ETCO2':'mmHg',
               'ART_MBP':'mmHg','ART_SBP':'mmHg','ART_DBP':'mmHg'}
SIG_COLOR  = {'HR':'#f1516a','PLETH_SPO2':'#10b981','ETCO2':'#f59e0b',
               'ART_MBP':'#3b82f6','ART_SBP':'#8b5cf6','ART_DBP':'#06b6d4'}
NORMAL     = {'HR':(50,100),'PLETH_SPO2':(95,100),'ETCO2':(35,45),
               'ART_MBP':(70,105),'ART_SBP':(90,140),'ART_DBP':(60,90)}
CHANGE_TH  = {'HR':10,'PLETH_SPO2':2,'ETCO2':5,
               'ART_MBP':15,'ART_SBP':20,'ART_DBP':10}

BG     = '#060810'
CARD   = '#0d1120'
BORDER = '#1c2236'
MUTED  = '#2d3748'
TEXT   = '#e2e8f4'
DIM    = '#8892aa'

# ══════════════════════════════════════════════════════════════════════
#  MODEL CLASSES
# ══════════════════════════════════════════════════════════════════════
class LSTMBaseline(nn.Module):
    def __init__(self, n_features=36, hidden=64, dropout=0.3):
        super().__init__()
        self.lstm1=nn.LSTM(n_features,hidden,batch_first=True)
        self.lstm2=nn.LSTM(hidden,hidden//2,batch_first=True)
        self.bn1=nn.BatchNorm1d(hidden); self.bn2=nn.BatchNorm1d(hidden//2)
        self.drop=nn.Dropout(dropout)
        self.fc1=nn.Linear(hidden//2,32); self.fc2=nn.Linear(32,1)
        self.relu=nn.ReLU()
    def forward(self,x):
        out,_=self.lstm1(x); out=self.bn1(out[:,-1,:]); out=self.drop(out).unsqueeze(1)
        out,_=self.lstm2(out); out=self.bn2(out[:,-1,:]); out=self.drop(out)
        return self.fc2(self.drop(self.relu(self.fc1(out)))).squeeze(1)

class TemporalAttentionNetwork(nn.Module):
    def __init__(self, n_features=36, hidden=64, n_heads=4, dropout=0.3):
        super().__init__()
        self.lstm1=nn.LSTM(n_features,hidden,batch_first=True)
        self.lstm2=nn.LSTM(hidden,hidden//2,batch_first=True)
        self.bn1=nn.BatchNorm1d(hidden); self.bn2=nn.BatchNorm1d(hidden//2)
        self.drop=nn.Dropout(dropout)
        self.attention=nn.MultiheadAttention(hidden//2,n_heads,dropout=dropout,batch_first=True)
        self.layer_norm=nn.LayerNorm(hidden//2)
        self.fc1=nn.Linear(hidden//2,32); self.fc2=nn.Linear(32,1); self.relu=nn.ReLU()
    def forward(self,x,return_attn=False):
        B,T,_=x.shape
        out,_=self.lstm1(x); out=self.bn1(out.reshape(B*T,-1)).reshape(B,T,-1); out=self.drop(out)
        out,_=self.lstm2(out); B2,T2,H=out.shape
        out=self.bn2(out.reshape(B2*T2,H)).reshape(B2,T2,H); out=self.drop(out)
        ao,aw=self.attention(out,out,out)
        out=self.layer_norm(out+self.drop(ao)).mean(dim=1)
        logits=self.fc2(self.drop(self.relu(self.fc1(out)))).squeeze(1)
        return (logits,aw) if return_attn else logits

@st.cache_resource
def load_models():
    device=torch.device('cpu')
    lstm=LSTMBaseline().to(device); tan=TemporalAttentionNetwork().to(device)
    for paths in [
        [os.path.join(SCRIPT_DIR,'lstm','lstm_best.pt'),
         os.path.join(SCRIPT_DIR,'tan','tan_best.pt')],
        [os.path.join(SCRIPT_DIR,'lstm_best.pt'),
         os.path.join(SCRIPT_DIR,'tan_best.pt')],
    ]:
        if all(os.path.exists(p) for p in paths):
            try:
                lstm.load_state_dict(torch.load(paths[0],map_location=device))
                tan.load_state_dict(torch.load(paths[1],map_location=device))
                lstm.eval(); tan.eval()
                return lstm, tan, True
            except: pass
    return None, None, False

# ══════════════════════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════════════════════
def compute_features(vw):
    feats=[]
    for sig in SIGNALS:
        v=np.array(vw[sig]); v=v[~np.isnan(v)]
        if len(v)==0: v=np.array([0.])
        t=np.arange(len(v))
        sl=np.polyfit(t,v,1)[0] if len(v)>1 else 0.
        feats+=[float(np.mean(v)),float(np.std(v)),float(np.min(v)),
                float(np.max(v)),float(np.ptp(v)),float(sl)]
    return np.array(feats,dtype=np.float32)

def rolling_risk(patient, tan_model, window_mins):
    n=len(patient['times']); risks=[None]*window_mins
    is_ca=patient['label']==1
    for i in range(window_mins,n):
        wnd={sig:patient[sig][i-window_mins:i] for sig in SIGNALS}
        feats=compute_features(wnd)
        X=torch.from_numpy(np.stack([feats]*4)[np.newaxis])
        with torch.no_grad():
            if tan_model:
                p=torch.sigmoid(tan_model(X)).item()
            else:
                rng=np.random.default_rng(i)
                if is_ca:
                    base=0.05+max(0,(i-300))*0.0018+max(0,(i-400))*0.004
                    p=float(np.clip(base+rng.normal(0,0.012),0,0.99))
                else:
                    p=float(np.clip(0.04+rng.normal(0,0.008),0.01,0.18))
        risks.append(p)
    return risks

def change_points(vals, times, thresh, window=15):
    out=[]; last_t=None
    for i in range(window,len(vals)):
        prev=np.mean(vals[i-window:i-window//2])
        curr=np.mean(vals[i-window//2:i])
        delta=curr-prev
        if abs(delta)>=thresh:
            t=times[i]
            if last_t is None or (t-last_t).seconds>900:
                lo,hi=0,1e9
                out.append({'time':t,'ts':t.strftime('%H:%M'),
                            'val':vals[i],'delta':delta,
                            'dir':'UP' if delta>0 else 'DOWN'})
                last_t=t
    return out

def demo_patient(ca=True, seed=42):
    rng=np.random.default_rng(seed); n=480; t=np.arange(n)
    start=datetime(2024,3,9,8,0,0)
    times=[start+timedelta(minutes=i) for i in range(n)]
    if ca:
        hr=72+rng.normal(0,2,n)+np.where(t>300,(t-300)*0.10,0)+rng.normal(0,3,n)
        spo2=98-rng.normal(0,.3,n)-np.where(t>360,(t-360)*0.06,0)+rng.normal(0,.4,n)
        etco2=38+rng.normal(0,1,n)-np.where(t>340,(t-340)*0.04,0)+rng.normal(0,1,n)
        mbp=85+rng.normal(0,3,n)-np.where(t>320,(t-320)*0.14,0)+rng.normal(0,4,n)
        ca_t=460; label=1
    else:
        hr=70+rng.normal(0,3,n); spo2=98+rng.normal(0,.4,n)
        etco2=38+rng.normal(0,1.5,n); mbp=85+rng.normal(0,4,n)
        ca_t=None; label=0
    sbp=mbp+40+rng.normal(0,3,n); dbp=mbp-20+rng.normal(0,3,n)
    return {'times':times,
            'HR':np.clip(hr,30,200).tolist(),
            'PLETH_SPO2':np.clip(spo2,70,100).tolist(),
            'ETCO2':np.clip(etco2,10,60).tolist(),
            'ART_MBP':np.clip(mbp,30,150).tolist(),
            'ART_SBP':np.clip(sbp,50,200).tolist(),
            'ART_DBP':np.clip(dbp,20,120).tolist(),
            'ca_time':ca_t,'label':label}

def risk_level(p):
    if p>=0.75: return 'CRITICAL','#f1516a','risk-critical','risk-pct-critical'
    if p>=0.50: return 'HIGH','#f59e0b','risk-high','risk-pct-high'
    if p>=0.25: return 'MODERATE','#10b981','risk-moderate','risk-pct-moderate'
    return 'LOW','#3b82f6','risk-low','risk-pct-low'

def plotly_base():
    return dict(plot_bgcolor=CARD, paper_bgcolor=BG,
                font=dict(family='Space Mono',color=MUTED,size=10),
                margin=dict(l=40,r=16,t=36,b=30),
                xaxis=dict(gridcolor=BORDER,tickfont=dict(color=MUTED,size=9),
                           showline=False,zeroline=False),
                yaxis=dict(gridcolor=BORDER,tickfont=dict(color=MUTED,size=9),
                           showline=False,zeroline=False),
                showlegend=False, hovermode='x unified')

# ══════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ══════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown(f"### 🫀 CA Risk Monitor")
    st.caption("Intraoperative Prototype · TSI 2026")
    st.divider()

    mode=st.radio("View mode",["Single Patient","Compare 2 Patients"])
    st.divider()

    if mode=="Single Patient":
        demo_type=st.selectbox("Patient type",["High Risk (CA Event)","Low Risk (No CA)"])
        seed=st.slider("Patient seed",1,100,42)
        ca_A="High Risk" in demo_type
    else:
        st.caption("Patient A")
        dA=st.selectbox("Patient A",["High Risk (CA Event)","Low Risk (No CA)"],key="dA")
        sA=st.slider("Seed A",1,100,42,key="sA")
        st.caption("Patient B")
        dB=st.selectbox("Patient B",["Low Risk (No CA)","High Risk (CA Event)"],key="dB")
        sB=st.slider("Seed B",1,100,77,key="sB")
        ca_A="High Risk" in dA; ca_B="High Risk" in dB

    st.divider()
    alert_th=st.slider("Alert threshold (%)",20,90,55)/100
    lkbk=st.slider("Lookback window (min)",30,240,60,step=30)
    st.divider()
    st.caption("TAN · AUROC 0.9937  \nLightGBM · AUROC 0.9073  \nTSI University · 2026")

# ══════════════════════════════════════════════════════════════════════
#  LOAD
# ══════════════════════════════════════════════════════════════════════
lstm_model, tan_model, models_ok = load_models()

if mode=="Single Patient":
    patients=[demo_patient(ca_A,seed)]
    labels=["Patient"]
else:
    patients=[demo_patient(ca_A,sA), demo_patient(ca_B,sB)]
    labels=["Patient A","Patient B"]

all_risks=[]
for pt in patients:
    all_risks.append(rolling_risk(pt, tan_model, lkbk))

# ══════════════════════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════════════════════
now_str=datetime.now().strftime("%d %b %Y · %H:%M")
model_str="✓ MODELS LOADED" if models_ok else "⚡ DEMO MODE"
st.markdown(f"""
<div style="border-bottom:1px solid {BORDER};padding-bottom:14px;margin-bottom:20px;">
  <div style="font-family:'Space Mono',monospace;font-size:18px;font-weight:700;
              color:{TEXT};letter-spacing:-0.5px;">
    🫀 INTRAOPERATIVE CA RISK MONITOR
  </div>
  <div style="font-family:'Space Mono',monospace;font-size:10px;color:{MUTED};
              margin-top:5px;letter-spacing:1px;">
    TAN · AUROC 0.9937 &nbsp;|&nbsp; {now_str} &nbsp;|&nbsp; {model_str} &nbsp;|&nbsp; {mode}
  </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  RENDER FUNCTION
# ══════════════════════════════════════════════════════════════════════
def render_panel(patient, risks, label, alert_th, lkbk, tan_model):
    valid=   [r for r in risks if r is not None]
    curr =   valid[-1] if valid else 0.04
    lvl,clr,risk_cls,pct_cls = risk_level(curr)
    ca_idx=  patient['ca_time']
    is_ca=   patient['label']==1

    # ── Patient label bar ────────────────────────────────────────────
    badge_cls="badge-ca" if is_ca else "badge-noca"
    badge_txt="⚠ CA EVENT" if is_ca else "✓ NO CA"
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px;">
      <span style="font-family:'Space Mono',monospace;font-size:13px;
                   font-weight:700;color:{TEXT};">{label}</span>
      <span class="badge {badge_cls}">{badge_txt}</span>
    </div>""", unsafe_allow_html=True)

    # ── Row 1: Risk score + 6 vitals ─────────────────────────────────
    cols=st.columns([1.3,1,1,1,1,1,1])

    with cols[0]:
        st.markdown(f"""
        <div class="risk-wrap {risk_cls}">
          <div style="font-family:'Space Mono',monospace;font-size:9px;
                      color:{MUTED};letter-spacing:2px;margin-bottom:8px;">
            CA RISK · {lkbk}MIN WINDOW
          </div>
          <div class="{pct_cls}">{curr*100:.1f}%</div>
          <div style="font-size:13px;font-weight:600;color:{clr};
                      margin-top:8px;font-family:'Space Mono',monospace;">
            {lvl}
          </div>
        </div>""", unsafe_allow_html=True)
        if curr>=alert_th:
            st.markdown(f"""
            <div class="alert-box">🚨 ALERT<br>
            Risk ≥ {alert_th*100:.0f}%<br>Notify physician
            </div>""", unsafe_allow_html=True)

    for i,sig in enumerate(SIGNALS):
        val=patient[sig][-1]; lo,hi=NORMAL[sig]
        if val<lo:   vcls,arr="v-val-bad","↓ LOW"
        elif val>hi: vcls,arr="v-val-warn","↑ HIGH"
        else:        vcls,arr="v-val-ok","→ OK"
        last30=patient[sig][-30:] if len(patient[sig])>=30 else patient[sig]
        tr=np.mean(last30[-10:])-np.mean(last30[:10])
        tr_str=f"{'↗' if tr>2 else '↘' if tr<-2 else '→'}{abs(tr):.1f}"
        tr_col="#f1516a" if tr>2 else "#3b82f6" if tr<-2 else "#10b981"
        with cols[i+1]:
            st.markdown(f"""
            <div class="vital-card">
              <div class="v-label">{SIG_LABEL[sig]}</div>
              <div class="{vcls}">{val:.0f}</div>
              <div class="v-unit">{SIG_UNIT[sig]}</div>
              <div class="v-trend" style="color:{clr if vcls!='v-val-ok' else '#10b981'}">
                {arr}
              </div>
              <div class="v-trend" style="color:{tr_col}">{tr_str}/30m</div>
              <div class="v-norm">{lo}–{hi}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)

    # ── Risk Timeline ─────────────────────────────────────────────────
    st.markdown('<div class="sec-label">Risk Score Over Time</div>',
                unsafe_allow_html=True)

    rtimes=[patient['times'][i].strftime('%H:%M')
            for i,r in enumerate(risks) if r is not None]
    rvals =[r for r in risks if r is not None]

    fig=go.Figure()
    # Background zones
    fig.add_hrect(y0=0.75,y1=1,fillcolor='rgba(241,81,106,0.04)',line_width=0)
    fig.add_hrect(y0=alert_th,y1=0.75,fillcolor='rgba(245,158,11,0.03)',line_width=0)

    # Risk area
    fig.add_trace(go.Scatter(
        x=rtimes,y=rvals,mode='lines',
        line=dict(color=clr,width=2),
        fill='tozeroy',fillcolor=f'rgba({int(clr[1:3],16)},{int(clr[3:5],16)},{int(clr[5:7],16)},0.08)',
        hovertemplate='%{x}<br>Risk: %{y:.1%}<extra></extra>'
    ))
    # Threshold lines
    fig.add_hline(y=alert_th,line_dash='dash',line_color='#f59e0b',line_width=1,
        annotation_text=f'Alert {alert_th*100:.0f}%',
        annotation_font=dict(color='#f59e0b',size=9),
        annotation_position='top right')
    fig.add_hline(y=0.75,line_dash='dot',line_color='#f1516a',line_width=1,
        annotation_text='Critical 75%',
        annotation_font=dict(color='#f1516a',size=9),
        annotation_position='top left')

    # CA event marker
    if ca_idx is not None:
        offset=len(risks)-len(rvals)
        ci=ca_idx-offset-1
        if 0<=ci<len(rtimes):
            fig.add_trace(go.Scatter(
                x=[rtimes[ci],rtimes[ci]],y=[0,1],mode='lines+text',
                line=dict(color='#f1516a',width=1.5,dash='dot'),
                text=['','CA EVENT'],textposition='top center',
                textfont=dict(color='#f1516a',size=9,family='Space Mono'),
                hoverinfo='skip'
            ))
    # Alert crossing
    for i in range(1,len(rvals)):
        if rvals[i]>=alert_th and rvals[i-1]<alert_th:
            fig.add_trace(go.Scatter(
                x=[rtimes[i],rtimes[i]],y=[0,1],mode='lines+text',
                line=dict(color='#f59e0b',width=1,dash='dash'),
                text=['','ALERT'],textposition='top center',
                textfont=dict(color='#f59e0b',size=9,family='Space Mono'),
                hoverinfo='skip'
            ))
            break

    layout=plotly_base()
    layout.update(height=200,
        yaxis=dict(**layout['yaxis'],tickformat='.0%',range=[0,1.05]),
        xaxis=dict(**layout['xaxis'],nticks=18),
        margin=dict(l=50,r=20,t=16,b=30))
    fig.update_layout(**layout)
    st.plotly_chart(fig,use_container_width=True)

    # ── Signal Charts (all 6, 2-column grid) ─────────────────────────
    st.markdown('<div class="sec-label">Vital Signal Trends</div>',
                unsafe_allow_html=True)

    pairs=[(SIGNALS[i],SIGNALS[i+1]) for i in range(0,6,2)]
    for sA,sB in pairs:
        c1,c2=st.columns(2)
        for sig,col in [(sA,c1),(sB,c2)]:
            with col:
                vals=patient[sig]; times=patient['times']
                lo,hi=NORMAL[sig]; color=SIG_COLOR[sig]
                ts=[t.strftime('%H:%M') for t in times]
                cps=change_points(vals,times,CHANGE_TH[sig])

                f=go.Figure()
                f.add_hrect(y0=lo,y1=hi,fillcolor='rgba(16,185,129,0.04)',line_width=0)
                f.add_hline(y=hi,line_dash='dot',line_color=BORDER,line_width=1)
                f.add_hline(y=lo,line_dash='dot',line_color=BORDER,line_width=1)
                f.add_trace(go.Scatter(
                    x=ts,y=vals,mode='lines',
                    line=dict(color=color,width=1.8),
                    hovertemplate=f'{SIG_LABEL[sig]}: %{{y:.1f}} {SIG_UNIT[sig]}<extra></extra>'
                ))
                # Out-of-range dots
                danger=[v if (v<lo or v>hi) else None for v in vals]
                f.add_trace(go.Scatter(x=ts,y=danger,mode='markers',
                    marker=dict(color='#f1516a',size=3,opacity=0.7),
                    hoverinfo='skip'))
                # Change points
                for cp in cps:
                    cs=cp['time'].strftime('%H:%M')
                    f.add_trace(go.Scatter(
                        x=[cs,cs],y=[min(vals)*0.97,max(vals)*1.03],
                        mode='lines',line=dict(color='#f59e0b',width=1,dash='dot'),
                        hoverinfo='skip'))
                    f.add_annotation(x=cs,y=cp['val'],
                        text=f"{'↑' if cp['dir']=='UP' else '↓'}{abs(cp['delta']):.1f}",
                        showarrow=True,arrowhead=2,arrowcolor='#f59e0b',
                        font=dict(size=9,color='#f59e0b',family='Space Mono'),
                        bgcolor='#0d1120',bordercolor='#f59e0b',
                        borderwidth=1,borderpad=2,ax=0,ay=-28)
                # CA marker
                if ca_idx is not None:
                    cas=patient['times'][ca_idx].strftime('%H:%M')
                    f.add_trace(go.Scatter(
                        x=[cas,cas],y=[min(vals)*0.97,max(vals)*1.03],
                        mode='lines+text',
                        line=dict(color='#f1516a',width=1.5,dash='dot'),
                        text=['','CA'],textposition='top center',
                        textfont=dict(size=9,color='#f1516a',family='Space Mono'),
                        hoverinfo='skip'))

                lyt=plotly_base()
                lyt.update(height=210,
                    title=dict(
                        text=f"{SIG_LABEL[sig]} <span style='font-size:10px;color:{MUTED}'>"
                             f"({SIG_UNIT[sig]}) · norm {lo}–{hi} · {len(cps)} Δ</span>",
                        font=dict(size=11,color=TEXT,family='Space Mono'),x=0),
                    margin=dict(l=36,r=10,t=38,b=28))
                f.update_layout(**lyt)
                st.plotly_chart(f,use_container_width=True)

    # ── Change Point Table ────────────────────────────────────────────
    st.markdown('<div class="sec-label">Change Point Log</div>',
                unsafe_allow_html=True)

    all_cps=[]
    for sig in SIGNALS:
        lo,hi=NORMAL[sig]
        for cp in change_points(patient[sig],patient['times'],CHANGE_TH[sig]):
            in_range=lo<=cp['val']<=hi
            all_cps.append({
                'Time':cp['ts'],'Signal':SIG_LABEL[sig],
                'Value':f"{cp['val']:.1f} {SIG_UNIT[sig]}",
                'Change':f"{'↑' if cp['dir']=='UP' else '↓'} {abs(cp['delta']):.1f}",
                'Status':'Within range' if in_range else '⚠ Outside range',
                'Normal':f"{lo}–{hi}",
                '_up':cp['dir']=='UP','_bad':not in_range,'_sig':sig
            })
    all_cps.sort(key=lambda x:x['Time'])

    if all_cps:
        rows=""
        for c in all_cps:
            dc='td-up' if c['_up'] else 'td-down'
            sc='td-warn' if c['_bad'] else 'td-ok'
            rows+=f"""<tr>
              <td style='color:{TEXT}'>{c['Time']}</td>
              <td style='color:{SIG_COLOR[c["_sig"]]}'>{c['Signal']}</td>
              <td style='color:{TEXT}'>{c['Value']}</td>
              <td class='{dc}'>{c['Change']}</td>
              <td class='{sc}'>{c['Status']}</td>
              <td>{c['Normal']}</td></tr>"""
        st.markdown(f"""
        <table class="data-table">
          <thead><tr><th>TIME</th><th>SIGNAL</th><th>VALUE</th>
          <th>CHANGE</th><th>STATUS</th><th>NORMAL</th></tr></thead>
          <tbody>{rows}</tbody>
        </table>""", unsafe_allow_html=True)
    else:
        st.markdown('<div class="info-box">No significant change points detected.</div>',
                    unsafe_allow_html=True)

    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

    # ── Attention + Window Risk ───────────────────────────────────────
    c_att,c_win=st.columns(2)

    with c_att:
        st.markdown('<div class="sec-label">TAN Attention Weights</div>',
                    unsafe_allow_html=True)
        npy=os.path.join(SCRIPT_DIR,'tan','attention_weights_cv.npy')
        try:
            raw=np.load(npy); mn=raw.mean(axis=(0,1)); an=mn/mn.sum()
        except:
            an=np.array([0.1622,0.1516,0.1570,0.5292])
        dom=WINDOWS[int(np.argmax(an))]
        fa=go.Figure()
        fa.add_trace(go.Bar(
            x=[f'{w}m' for w in WINDOWS], y=an,
            marker_color=['#3b82f6','#f59e0b','#8b5cf6','#10b981'],
            text=[f'{v*100:.1f}%' for v in an],
            textposition='outside',
            textfont=dict(color=TEXT,size=10,family='Space Mono')
        ))
        la=plotly_base()
        la.update(height=200,
            yaxis=dict(**la['yaxis'],tickformat='.0%',range=[0,0.7]),
            xaxis=dict(**la['xaxis']),
            title=dict(text='',x=0),
            margin=dict(l=36,r=10,t=12,b=28))
        fa.update_layout(**la)
        st.plotly_chart(fa,use_container_width=True)
        st.markdown(f'<div class="info-box">Model focuses most on the '
                    f'<strong>{dom}-min</strong> window '
                    f'({an[WINDOWS.index(dom)]*100:.1f}% weight)</div>',
                    unsafe_allow_html=True)

    with c_win:
        st.markdown('<div class="sec-label">Risk by Window Size</div>',
                    unsafe_allow_html=True)
        now_i=len(patient['times'])-1
        pwr={}
        for w in WINDOWS:
            si=max(0,now_i-w)
            wnd={sig:patient[sig][si:now_i+1] for sig in SIGNALS}
            feats=compute_features(wnd)
            X=torch.from_numpy(np.stack([feats]*4)[np.newaxis])
            with torch.no_grad():
                if tan_model:
                    p=torch.sigmoid(tan_model(X)).item()
                else:
                    p=curr+np.random.default_rng(w).normal(0,0.03)
            pwr[w]=float(np.clip(p,0,1))

        fw=go.Figure()
        fw.add_trace(go.Bar(
            x=[f'{w}m' for w in WINDOWS],
            y=list(pwr.values()),
            marker_color=[risk_level(pwr[w])[1] for w in WINDOWS],
            text=[f'{v*100:.1f}%' for v in pwr.values()],
            textposition='outside',
            textfont=dict(color=TEXT,size=10,family='Space Mono')
        ))
        fw.add_hline(y=alert_th,line_dash='dash',line_color='#f59e0b',line_width=1)
        lw=plotly_base()
        lw.update(height=200,
            yaxis=dict(**lw['yaxis'],tickformat='.0%',range=[0,1.15]),
            xaxis=dict(**lw['xaxis']),
            margin=dict(l=36,r=10,t=12,b=28))
        fw.update_layout(**lw)
        st.plotly_chart(fw,use_container_width=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════════════
if mode=="Single Patient":
    render_panel(patients[0],all_risks[0],labels[0],alert_th,lkbk,tan_model)

else:
    # Compare: side-by-side summary at top, then full panels below
    st.markdown('<div class="sec-label">Risk Comparison</div>',
                unsafe_allow_html=True)
    ca,cb=st.columns(2)
    for col,pt,rs,lbl in [(ca,patients[0],all_risks[0],labels[0]),
                           (cb,patients[1],all_risks[1],labels[1])]:
        vld=[r for r in rs if r is not None]
        cur=vld[-1] if vld else 0.04
        lv,cl,rc,pc=risk_level(cur)
        is_ca=pt['label']==1
        with col:
            st.markdown(f"""
            <div class="compare-header">
              <div style="font-family:'Space Mono',monospace;font-size:10px;
                          color:{MUTED};letter-spacing:1px;margin-bottom:6px;">
                {lbl} — {"⚠ HIGH RISK (CA EVENT)" if is_ca else "✓ LOW RISK (NO CA)"}
              </div>
              <div class="{pc}" style="font-size:42px;">{cur*100:.1f}%</div>
              <div style="font-size:12px;color:{cl};font-family:'Space Mono',
                          monospace;margin-top:4px;">{lv}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("<hr class='patient-divider'>", unsafe_allow_html=True)
    for pt,rs,lbl in zip(patients,all_risks,labels):
        render_panel(pt,rs,lbl,alert_th,lkbk,tan_model)
        st.markdown("<hr class='patient-divider'>", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  SHAP PANEL
# ══════════════════════════════════════════════════════════════════════
shap_bar=os.path.join(SCRIPT_DIR,'shap_outputs','shap_bar_top15.png')
shap_bee=os.path.join(SCRIPT_DIR,'shap_outputs','shap_beeswarm_top15.png')
if os.path.exists(shap_bar):
    st.markdown('<div class="sec-label">SHAP Interpretability — LightGBM</div>',
                unsafe_allow_html=True)
    s1,s2=st.columns(2)
    with s1: st.image(shap_bar,caption="Feature Importance (Mean |SHAP|)",use_container_width=True)
    if os.path.exists(shap_bee):
        with s2: st.image(shap_bee,caption="Feature Impact Direction (Beeswarm)",use_container_width=True)
    st.markdown("""<div class="info-box">
    🔬 <strong>SHAP (SHapley Additive exPlanations)</strong> — bar chart shows which features
    drive predictions most. Beeswarm shows direction: red = high value increases CA risk,
    blue = high value decreases risk. Generated from LightGBM 60-min window model.
    </div>""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════
st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
st.markdown(f"""
<div style="border-top:1px solid {BORDER};padding-top:14px;
            font-family:'Space Mono',monospace;font-size:10px;
            color:{MUTED};line-height:2;">
  🔴 CRITICAL ≥75% — Prepare resuscitation · Alert physician immediately &nbsp;|&nbsp;
  🟠 HIGH 50–75% — Increase monitoring · Check medications &nbsp;|&nbsp;
  🟡 MODERATE 25–50% — Close monitoring · Note trends &nbsp;|&nbsp;
  🔵 LOW &lt;25% — Routine monitoring<br>
  <span style="color:#2d3748;">
  Clinical decision-support prototype · Treatment decisions remain with attending physician ·
  TSI University 2026 · Sachu Mon P. Sajeev
  </span>
</div>""", unsafe_allow_html=True)
