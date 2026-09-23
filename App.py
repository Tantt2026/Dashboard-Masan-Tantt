import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta
import os
import datetime as dt

st.set_page_config(
    page_title="TRACKING KPI ĐDKD - SS Trương Thanh Tân",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================== LOGO ======================
logo_svg = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 158.15 61.91" width="110" height="42">
<title>Masan Group logo</title>
<path d="M490.29,502.16s17.83-12.81,45.76-12.93c25.9-.11,30.18,8.14,38,10.79,0,0-3.8,5.82-5.78,9.63s-13.32,17.93-26.5,22.21c0,0,18.71-15.72,21.55-27.57,0,0-26.87-20.43-73.26-1.92" transform="translate(-432.92 -481.05)" style="fill:#f36f21"/>
<path d="M521.55,489.11c42-10.64,59.59,9.56,59.59,9.56A60.39,60.39,0,0,1,561,521.3c11.28-1.28,21.79-13,24-16.69s6.16-9.17,6.16-9.17c-7.12-3.22-13.13-12-35.93-14.22-16.3-1.59-33.6,7.88-33.6,7.88" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M454.12,528V512.92a58.92,58.92,0,0,1-.15-6.31l-.06,0-7.1,21.11h-3.41l-7.25-21h-.09c0,2.33.1,5.52.09,6.28v15h-3.24V502.39h4.8L445.1,524h.07l7.17-21.31h5V528Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M465.15,515c.21-1.42.7-3.56,4.21-3.58,2.94,0,4.35,1,4.37,3s-.87,2.12-1.62,2.19l-5.11.65c-5.13.67-5.58,4.26-5.57,5.81,0,3.16,2.42,5.3,5.8,5.29a8.32,8.32,0,0,0,6.64-3c.12,1.42.55,2.82,3.3,2.81a6.24,6.24,0,0,0,1.69-.36v-2.26a4.84,4.84,0,0,1-1,.14c-.63,0-1-.3-1-1.09l-.05-10.6c0-4.73-5.37-5.13-6.85-5.13-4.54,0-7.47,1.76-7.6,6.17Zm8.42,6.37c0,2.48-2.85,4.35-5.74,4.36-2.35,0-3.38-1.17-3.39-3.19,0-2.32,2.42-2.8,4-3,3.86-.52,4.64-.78,5.15-1.18Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M492.47,514.47c0-1.17-.47-3.12-4.44-3.1-1,0-3.7.34-3.7,2.64,0,1.53,1,1.88,3.4,2.46l3.14.77c3.89.94,5.27,2.35,5.27,4.87,0,3.83-3.15,6.14-7.37,6.16-7.39,0-7.94-4.21-8-6.44h3c.11,1.45.55,3.78,5,3.75,2.24,0,4.27-.89,4.26-3,0-1.47-1-2-3.72-2.63l-3.65-.88c-2.59-.62-4.31-1.91-4.34-4.46,0-4.09,3.39-6,7.05-6,6.66,0,7.17,4.87,7.17,5.78Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M502.6,514.75c.2-1.42.68-3.58,4.2-3.6,2.91,0,4.33,1.06,4.33,3s-.86,2.13-1.61,2.18l-5.1.66c-5.11.65-5.57,4.27-5.56,5.79,0,3.19,2.41,5.31,5.79,5.31a8.34,8.34,0,0,0,6.63-3c.11,1.41.53,2.83,3.28,2.8a5.87,5.87,0,0,0,1.68-.35l0-2.26a6.5,6.5,0,0,1-1,.15c-.62,0-1-.32-1-1.1l0-10.61c0-4.72-5.35-5.11-6.83-5.11-4.53,0-7.44,1.76-7.56,6.16Zm8.36,6.49c0,2.47-2.82,4.36-5.74,4.37-2.35,0-3.37-1.18-3.39-3.18,0-2.34,2.44-2.8,4-3,3.87-.51,4.65-.8,5.14-1.2Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M534.55,527.71h-3v-11.5c-.13-3.2-1.07-4.83-4.13-4.81-1.77,0-4.88,1.15-4.7,6.15v10.16h-3.24l-.07-18.56h2.72l0,2.66h.07a6.85,6.85,0,0,1,5.67-3.19c2.91,0,6.58,1.15,6.6,6.45Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M468,533.85a1.19,1.19,0,0,1,.07.34.6.6,0,0,1-.19.46.81.81,0,0,1-.51.21l-.54-.18q-.45-.15-.75-.23a2.37,2.37,0,0,0-.59-.08,2.27,2.27,0,0,0-1.47.49,3.1,3.1,0,0,0-.92,1.27,4.89,4.89,0,0,0-.35,1.64,5.25,5.25,0,0,0,.56,2.41,2.27,2.27,0,0,0,1.91,1.26.77.77,0,0,1,.27,0l.43-.06.37-.1.37-.15L467,541a1,1,0,0,1,.4-.11.54.54,0,0,1,.42.19.69.69,0,0,1,.17.48,1,1,0,0,1-.82,1,5.35,5.35,0,0,1-1.69.27,4.1,4.1,0,0,1-2.28-.63,4.15,4.15,0,0,1-1.5-1.71,5.52,5.52,0,0,1-.55-2.35,7.3,7.3,0,0,1,.25-1.93,5,5,0,0,1,.76-1.63,3.74,3.74,0,0,1,1.34-1.14,4.33,4.33,0,0,1,1.91-.45,4.73,4.73,0,0,1,1.68.27,1.72,1.72,0,0,1,.91.62" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M470.75,537.9a4.78,4.78,0,0,0,.63,2.45,2.13,2.13,0,0,0,2,1.1,2.3,2.3,0,0,0,1.48-.48,2.78,2.78,0,0,0,.88-1.28,5.69,5.69,0,0,0,.31-1.78,5.11,5.11,0,0,0-.3-1.78,2.94,2.94,0,0,0-.89-1.29,2.21,2.21,0,0,0-1.44-.48,2.3,2.3,0,0,0-1.44.46,2.82,2.82,0,0,0-.91,1.27,5.12,5.12,0,0,0-.31,1.82m-1.59,0a5.74,5.74,0,0,1,.54-2.53,4.26,4.26,0,0,1,1.51-1.76,4,4,0,0,1,4.42.06,4.39,4.39,0,0,1,1.47,1.8,5.8,5.8,0,0,1,.51,2.43,5.89,5.89,0,0,1-.51,2.46,4.25,4.25,0,0,1-1.47,1.79,4.11,4.11,0,0,1-4.49,0,4.31,4.31,0,0,1-1.48-1.8,5.85,5.85,0,0,1-.51-2.44" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M479.44,534.07a.79.79,0,0,1,.21-.58.7.7,0,0,1,.52-.21.73.73,0,0,1,.53.21.78.78,0,0,1,.22.59v.14l0,0a3,3,0,0,1,1.13-.91,3.31,3.31,0,0,1,1.43-.32,3.46,3.46,0,0,1,1.63.4,3,3,0,0,1,1.21,1.21,4,4,0,0,1,.46,2V542a.68.68,0,0,1-.22.54.77.77,0,0,1-.53.19.73.73,0,0,1-.51-.19.69.69,0,0,1-.21-.53v-5.36a2.16,2.16,0,0,0-.65-1.67,2.21,2.21,0,0,0-1.55-.6,2.32,2.32,0,0,0-1.09.26,2,2,0,0,0-.82.79,2.41,2.41,0,0,0-.31,1.25v5.05a.81.81,0,0,1-.2.59.68.68,0,0,1-.51.21.74.74,0,0,1-.54-.22.77.77,0,0,1-.23-.58Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M488.69,541.75a1.05,1.05,0,0,1-.44-.77.7.7,0,0,1,.2-.49.64.64,0,0,1,.49-.21,1,1,0,0,1,.46.13,6.25,6.25,0,0,1,.57.37,3.06,3.06,0,0,0,.49.31,3,3,0,0,0,1.34.36,2.88,2.88,0,0,0,1.37-.32,1.06,1.06,0,0,0,.6-1A1.24,1.24,0,0,0,493,539a9.34,9.34,0,0,0-1.39-.65q-1-.4-1.55-.68a3.05,3.05,0,0,1-1-.79,1.94,1.94,0,0,1-.42-1.28,2.36,2.36,0,0,1,.39-1.31,2.79,2.79,0,0,1,1.11-1,4,4,0,0,1,1.64-.4,5,5,0,0,1,1.71.3,3.57,3.57,0,0,1,1.22.66,1.1,1.1,0,0,1,.38.74.65.65,0,0,1-.21.47.78.78,0,0,1-.5.23,4.06,4.06,0,0,1-.89-.41c-.39-.22-.67-.38-.86-.46a1.78,1.78,0,0,0-.69-.15,2,2,0,0,0-1.28.35,1.16,1.16,0,0,0-.46.86,1.34,1.34,0,0,0,.42.75,2.92,2.92,0,0,0,.78.52q.44.2,1.07.41c.42.14.71.25.87.32a3.77,3.77,0,0,1,1.54,1,2.2,2.2,0,0,1,.47,1.42,2.72,2.72,0,0,1-.42,1.37,2.86,2.86,0,0,1-1.19,1,4.49,4.49,0,0,1-2,.41,4.67,4.67,0,0,1-3.14-1.06" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M496.81,533.76a.74.74,0,0,1,.21-.56.71.71,0,0,1,.52-.21.74.74,0,0,1,.53.2.73.73,0,0,1,.22.56V539a2.75,2.75,0,0,0,.58,1.85,2.16,2.16,0,0,0,1.74.69q2.38,0,2.38-2.53v-5.22a.74.74,0,0,1,.21-.56.71.71,0,0,1,.51-.21.74.74,0,0,1,.53.2.73.73,0,0,1,.22.56v5.3a4.35,4.35,0,0,1-.4,1.86,3.14,3.14,0,0,1-1.27,1.38,4.23,4.23,0,0,1-2.22.53,4,4,0,0,1-2.11-.51,3.14,3.14,0,0,1-1.25-1.37,4.36,4.36,0,0,1-.4-1.88Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M506.53,533.81a.7.7,0,0,1,.22-.53.76.76,0,0,1,.54-.21.68.68,0,0,1,.51.2.84.84,0,0,1,.2.61v.3h.94a2.69,2.69,0,0,1,2.29-1.15,2.75,2.75,0,0,1,2.4,1.62,3.7,3.7,0,0,1,1.29-1.26,3.26,3.26,0,0,1,1.53-.36,3,3,0,0,1,1.52.44,3,3,0,0,1,1.1,1.21,3.92,3.92,0,0,1,.41,1.84v5.58a.74.74,0,0,1-.22.57.74.74,0,0,1-.53.21.7.7,0,0,1-.5-.22.76.76,0,0,1-.22-.56v-5.54a2.57,2.57,0,0,0-.27-1.21,1.78,1.78,0,0,0-.72-.76,2.08,2.08,0,0,0-1-.25,2.2,2.2,0,0,0-1.51.53,2.14,2.14,0,0,0-.6,1.69v5.5a.62.62,0,0,1-.22.51.8.8,0,0,1-.53.18.75.75,0,0,1-.5-.18.63.63,0,0,1-.22-.5v-5.34a2.48,2.48,0,0,0-.63-1.87,2.18,2.18,0,0,0-1.57-.6,2.85,2.85,0,0,0-1.12.26,1.84,1.84,0,0,0-.8.74,2.45,2.45,0,0,0-.3,1.28v5.57a.75.75,0,0,1-.22.57.73.73,0,0,1-.52.21.7.7,0,0,1-.51-.22.75.75,0,0,1-.22-.56Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M522.43,537.42h5.42a3.31,3.31,0,0,0-.7-2.13,2.38,2.38,0,0,0-1.86-.83,2.53,2.53,0,0,0-1.94.78,3.25,3.25,0,0,0-.79,2.18m-1.59.47a6.14,6.14,0,0,1,.56-2.34,4.52,4.52,0,0,1,1.46-1.79,3.92,3.92,0,0,1,4.43,0,4.44,4.44,0,0,1,1.49,1.78,5.34,5.34,0,0,1,.53,2.31q0,.78-.88.78h-6a3.22,3.22,0,0,0,.41,1.62,2.5,2.5,0,0,0,1.05,1,3.23,3.23,0,0,0,1.46.33,3.91,3.91,0,0,0,2.58-1,1.26,1.26,0,0,1,.6-.29.49.49,0,0,1,.41.2.78.78,0,0,1,.15.47.9.9,0,0,1-.23.58,4.46,4.46,0,0,1-1.5,1,5.2,5.2,0,0,1-2.09.42,4.42,4.42,0,0,1-2-.44,3.84,3.84,0,0,1-1.39-1.17,5,5,0,0,1-.77-1.58,6.65,6.65,0,0,1-.26-1.72l0-.06v0" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
<path d="M531,534a.83.83,0,0,1,.21-.59.69.69,0,0,1,.52-.22.72.72,0,0,1,.53.22.81.81,0,0,1,.22.6v.81h0a4.3,4.3,0,0,1,.87-1.13,1.77,1.77,0,0,1,1.13-.53.85.85,0,0,1,.59.23.76.76,0,0,1,.26.58.69.69,0,0,1-.26.6,2.4,2.4,0,0,1-.76.33,3.19,3.19,0,0,0-.65.23,2.54,2.54,0,0,0-1.2,2.4v4.66a.84.84,0,0,1-.2.6.68.68,0,0,1-.51.21.73.73,0,0,1-.54-.22.86.86,0,0,1-.22-.63Z" transform="translate(-432.92 -481.05)" style="fill:#034ea2"/>
</svg>
"""

# ====================== CSS ======================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1a365d 0%, #2b6cb0 100%);
        color: white;
        padding: 8px 12px;
        border-radius: 8px;
        margin-bottom: 10px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.12);
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .main-header .logo {
        flex-shrink: 0;
        background: white;
        border-radius: 6px;
        padding: 4px 6px;
        display: flex;
        align-items: center;
    }
    .main-header .title-block { flex: 1; text-align: center; }
    .main-header h1 {
        margin: 0;
        font-size: 18px;
        font-weight: 800;
        letter-spacing: 0.5px;
        line-height: 1.2;
    }
    .main-header h2 {
        margin: 2px 0 0 0;
        font-size: 12px;
        font-weight: 600;
        color: #fefcbf;
        letter-spacing: 0.3px;
    }
    .filter-label {
        font-weight: 700 !important;
        color: #c53030 !important;
        font-size: 11px !important;
        margin-bottom: 2px;
    }
    .note-box {
        background: #ebf8ff;
        border-left: 4px solid #3182ce;
        padding: 8px 12px;
        border-radius: 0 6px 6px 0;
        margin-top: 10px;
        font-size: 12px;
        line-height: 1.4;
    }
    footer {visibility: hidden;}
    #MainMenu, header {visibility: visible !important;}
    
    .custom-kpi-table {
        width: 100%;
        border-collapse: collapse;
        border: 1px solid #e2e8f0 !important;
        font-family: sans-serif;
        font-size: 11px;
        background-color: #ffffff;
    }
    .custom-kpi-table th {
        background-color: #f7fafc !important;
        color: #9b2c2c !important;
        font-weight: bold !important;
        text-align: center !important;
        border: 1px solid #e2e8f0 !important;
        padding: 5px 4px;
        white-space: nowrap;
    }
    .custom-kpi-table td {
        border: 1px solid #e2e8f0 !important;
        padding: 4px 5px;
    }
</style>
""", unsafe_allow_html=True)

def render_metric_card(label, value):
    st.markdown(f"""
    <div style="background: #ebf8ff; border: 1px solid #bee3f8; border-radius: 6px; padding: 8px; text-align: center; box-shadow: 0 1px 4px rgba(0,0,0,0.04); margin-bottom: 6px;">
        <div style="color: #c53030; font-weight: 800; font-size: 0.95rem; margin-bottom: 2px;">{label}</div>
        <div style="color: #c53030; font-weight: 800; font-size: 1.5rem;">{value}</div>
    </div>
    """, unsafe_allow_html=True)

# ====================== ĐƯỜNG DẪN ======================
DATA_DIR = "data"
RPT_PATH   = os.path.join(DATA_DIR, "RPT_061.xlsx")
MCP_PATH   = os.path.join(DATA_DIR, "Data_MCP.xlsx")
KPI_PATH   = os.path.join(DATA_DIR, "Target_KPI.xlsx")
CAT_PATH   = "Data_Cat.xlsx"
BRAND_PATH = "Data_Brand.xlsx"

# ====================== LOAD ======================
@st.cache_data(ttl=600)
def load_main_data():
    if not os.path.exists(RPT_PATH) or not os.path.exists(MCP_PATH):
        # Tạo thư mục data nếu chưa có
        os.makedirs(DATA_DIR, exist_ok=True)
    df = pd.read_excel(RPT_PATH) if os.path.exists(RPT_PATH) else pd.DataFrame()
    mcp = pd.read_excel(MCP_PATH) if os.path.exists(MCP_PATH) else pd.DataFrame()
    if not df.empty:
        if 'Tình trạng đơn hàng' in df.columns:
            df = df[df['Tình trạng đơn hàng'] != 'Đã hủy'].copy()
        if 'Ngày tạo đơn hàng' in df.columns:
            df['Ngày tạo đơn hàng'] = pd.to_datetime(df['Ngày tạo đơn hàng'], format='%d/%m/%Y %H:%M:%S', errors='coerce')
            df['date'] = df['Ngày tạo đơn hàng'].dt.date
        if 'Mã CH' in df.columns and 'Outlet_code' in mcp.columns:
            mcp_map = mcp[['Outlet_code', 'L1']].drop_duplicates('Outlet_code')
            mcp_map['Outlet_code'] = mcp_map['Outlet_code'].astype(str)
            df['Mã CH'] = df['Mã CH'].astype(str)
            df = df.merge(mcp_map, left_on='Mã CH', right_on='Outlet_code', how='left')
        if 'Tên sản phẩm' in df.columns:
            df['Tên SP lower'] = df['Tên sản phẩm'].astype(str).str.lower()
    return df, mcp

@st.cache_data(ttl=600)
def get_targets():
    if not os.path.exists(KPI_PATH): return {}
    try:
        kpi = pd.read_excel(KPI_PATH, header=None).iloc[2:]
        kpi.columns = ['Region','Month','Ship to','Distributor','SUP','SM pos','SM code','SM name',
                       'Saleteam','KPI type','KPI Name','Target','Thực hiện','% actual','% Contrib','Chưa ra HĐ']
        kpi = kpi.dropna(subset=['SM code'])
        kpi['Target'] = pd.to_numeric(kpi['Target'], errors='coerce')
        targets = {}
        for _, r in kpi.iterrows():
            sm, ktype, kname, tgt = str(r['SM code']).strip(), str(r['KPI type']).strip(), str(r['KPI Name']).strip(), r['Target']
            if pd.isna(tgt): continue
            ktype_lower, kname_lower = ktype.lower(), kname.lower()
            if ktype_lower == 'aso_all': targets.setdefault(sm, {})['ASO_ALL'] = int(tgt)
            elif ktype_lower == 'pc_bt': targets.setdefault(sm, {})['PC_BT'] = int(tgt)
            elif ktype_lower == 'aso_on': targets.setdefault(sm, {})['ASO_ON'] = int(tgt)
            elif ktype_lower == 'aso_focus' or 'xanh' in kname_lower: targets.setdefault(sm, {})['ASO_CHANTE'] = int(tgt)
            elif ktype_lower == 'aso_focus_2' or 'vàng' in kname_lower or 'trận vàng' in kname_lower: targets.setdefault(sm, {})['ASO_OMACHI'] = int(tgt)
        return targets
    except: return {}

@st.cache_data(ttl=600)
def get_turnover_targets():
    if not os.path.exists(KPI_PATH): return {}
    try:
        kpi = pd.read_excel(KPI_PATH, header=None).iloc[2:]
        kpi.columns = ['Region','Month','Ship to','Distributor','SUP','SM pos','SM code','SM name',
                       'Saleteam','KPI type','KPI Name','Target','Thực hiện','% actual','% Contrib','Chưa ra HĐ']
        kpi = kpi.dropna(subset=['SM code'])
        kpi['Target'] = pd.to_numeric(kpi['Target'], errors='coerce')
        targets = {}
        for _, r in kpi.iterrows():
            sm, ktype = str(r['SM code']).strip(), str(r['KPI type']).strip().lower()
            tgt = r['Target']
            if pd.isna(tgt): continue
            if ktype == 'turnover': targets[sm] = float(tgt)
        return targets
    except: return {}

def find_col(df, candidates):
    cols = {c.lower().strip(): c for c in df.columns}
    for c in candidates:
        if c.lower() in cols: return cols[c.lower()]
    return None

def color_pct_bg(val):
    try:
        v = float(str(val).replace('%','').strip())
        if v >= 70: return 'background-color: #c6f6d5; color:#22543d; font-weight:600;'
        elif v >= 50: return 'background-color: #fefcbf; color:#744210; font-weight:600;'
        else: return 'background-color: #fed7d7; color:#742a2a; font-weight:600;'
    except: return ''

def render_html_table(df):
    html = ['<div style="overflow-x: auto; -webkit-overflow-scrolling: touch;"><table class="custom-kpi-table">']
    html.append('<thead><tr>')
    for col in df.columns:
        html.append(f'<th>{col}</th>')
    html.append('</tr></thead><tbody>')
    for _, row in df.iterrows():
        is_total = str(row.get('Tên NVBH', '')).strip() == 'TỔNG CỘNG' or str(row.get('Tên NV', '')).strip() == 'TỔNG CỘNG'
        html.append('<tr>')
        for col in df.columns:
            val = row[col]
            if pd.isna(val): val = ""
            if col in ['% MTD', '% MTD (OFF)', '% MTD (ON)']:
                style_bg = color_pct_bg(val)
                html.append(f'<td style="{style_bg} text-align: center;">{val}</td>')
            elif is_total:
                align = 'left' if col in ['Tên NVBH', 'Tên NV'] else ('center' if col in ['STT', 'Mã NVBH'] else 'right')
                html.append(f'<td style="background-color: #fff5f5; color: #c53030 !important; font-weight: 900 !important; text-align: {align}; white-space: nowrap;">{val}</td>')
            elif col in ['Tên NVBH', 'Tên NV']:
                html.append(f'<td style="color: #1a365d; text-align: left; white-space: nowrap;">{val}</td>')
            else:
                align = 'center' if col in ['STT', 'Mã NVBH', 'Nhóm KH VIP3', 'Nhóm KH VIP5', 'Nhóm KH VIPSI', 'Nhóm KH CH Lẻ', 'Nhóm KH Kênh ON', 'Lịch Viếng Thăm Hôm Nay'] else 'right'
                html.append(f'<td style="text-align: {align}; white-space: nowrap;">{val}</td>')
        html.append('</tr>')
    html.append('</tbody></table></div>')
    return "".join(html)

# ====================== LOGIC BÁO CÁO LỊCH VIẾNG THĂM ======================
def build_visit_schedule_report(df_mcp, report_date, filter_nv=None):
    if df_mcp.empty:
        return pd.DataFrame(), "10. BÁO CÁO LỊCH VIẾNG THĂM"
    
    df = df_mcp.copy()
    
    # 1. Lọc Sup = '24SF16806-Trương Thanh Tân' hoặc tương ứng
    c_sup = find_col(df, ['Sup', 'SUP', 'Sales Sup', 'Supervisors'])
    if c_sup:
        df = df[df[c_sup].astype(str).str.contains('Trương Thanh Tân|24SF16806', case=False, na=False)]
    
    # 2. Lọc theo Thứ trong tuần
    wday = report_date.weekday() # 0:Mon -> 5:Sat, 6:Sun
    day_map = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday'}
    target_day = day_map.get(wday)
    
    c_day = find_col(df, [target_day, target_day.lower() if target_day else '']) if target_day else None
    if c_day and c_day in df.columns:
        df = df[df[c_day].astype(str).str.upper().str.strip() == 'Y']
        
    # 3. Lọc theo Tuần ISO (Odd/Even Week)
    iso_year, iso_week, iso_day = report_date.isocalendar()
    is_odd = (iso_week % 2 != 0)
    c_odd = find_col(df, ['ODD_WEEK', 'Odd_Week', 'Odd Week', 'Week Type'])
    if c_odd and c_odd in df.columns:
        if is_odd:
            df = df[df[c_odd].astype(str).str.strip().isin(['Odd Week', 'Both', 'ODD', 'BOTH'])]
        else:
            df = df[df[c_odd].astype(str).str.strip().isin(['Even Week', 'Both', 'EVEN', 'BOTH'])]
            
    # Lọc theo ĐDKD nếu chọn cụ thể
    c_nv_name = find_col(df, ['SM name', 'SM Name', 'Tên NVBH', 'Nhân viên'])
    c_nv_code = find_col(df, ['SM code', 'Mã NVBH', 'SM Code'])
    
    if filter_nv and filter_nv != "Tất cả ĐDKD" and c_nv_name:
        df = df[df[c_nv_name].astype(str).str.strip() == filter_nv.strip()]
        
    # 4. Phân loại 5 Nhóm Loại Trừ Lẫn Nhau
    c_l1 = find_col(df, ['L1', 'Channel'])
    c_vip = find_col(df, ['VIP MCH', 'VIP_MCH'])
    
    if c_l1 and c_vip:
        df['L1_str'] = df[c_l1].astype(str).str.strip()
        df['VIP_str'] = df[c_vip].astype(str).str.upper().str.strip()
        
        df['Is_ON'] = df['L1_str'].str.contains('On Premise', case=False, na=False)
        df['Is_VIP3'] = df['L1_str'].str.contains('Off Premise', case=False, na=False) & (df['VIP_str'] == 'VIP3')
        df['Is_VIP5'] = df['L1_str'].str.contains('Off Premise', case=False, na=False) & (df['VIP_str'] == 'VIP5')
        df['Is_VIPSI'] = df['L1_str'].str.contains('Off Premise', case=False, na=False) & (df['VIP_str'] == 'VIPSI')
        df['Is_CHLe'] = df['L1_str'].str.contains('Off Premise', case=False, na=False) & (~df['VIP_str'].isin(['VIP3', 'VIP5', 'VIPSI']))
    else:
        df['Is_ON'] = False
        df['Is_VIP3'] = False
        df['Is_VIP5'] = False
        df['Is_VIPSI'] = False
        df['Is_CHLe'] = True

    g_code = c_nv_code if c_nv_code else 'Mã NVBH'
    g_name = c_nv_name if c_nv_name else 'Tên NVBH'
    
    if g_code not in df.columns: df[g_code] = 'NV_CODE'
    if g_name not in df.columns: df[g_name] = 'NV_NAME'
    
    agg = df.groupby([g_code, g_name]).agg(
        VIP3=('Is_VIP3', 'sum'),
        VIP5=('Is_VIP5', 'sum'),
        VIPSI=('Is_VIPSI', 'sum'),
        CH_Le=('Is_CHLe', 'sum'),
        Kenh_ON=('Is_ON', 'sum')
    ).reset_index()
    
    agg['Tong'] = agg['VIP3'] + agg['VIP5'] + agg['VIPSI'] + agg['CH_Le'] + agg['Kenh_ON']
    
    rows = []
    for _, r in agg.iterrows():
        rows.append({
            'Mã NVBH': r[g_code],
            'Tên NVBH': r[g_name],
            'Nhóm KH VIP3': int(r['VIP3']),
            'Nhóm KH VIP5': int(r['VIP5']),
            'Nhóm KH VIPSI': int(r['VIPSI']),
            'Nhóm KH CH Lẻ': int(r['CH_Le']),
            'Nhóm KH Kênh ON': int(r['Kenh_ON']),
            'Lịch Viếng Thăm Hôm Nay': int(r['Tong'])
        })
        
    df_out = pd.DataFrame(rows)
    if not df_out.empty:
        df_out = df_out.sort_values(by='Lịch Viếng Thăm Hôm Nay', ascending=False).reset_index(drop=True)
        df_out.insert(0, 'STT', range(1, len(df_out) + 1))
        
        tot_v3 = int(df_out['Nhóm KH VIP3'].sum())
        tot_v5 = int(df_out['Nhóm KH VIP5'].sum())
        tot_vsi = int(df_out['Nhóm KH VIPSI'].sum())
        tot_chl = int(df_out['Nhóm KH CH Lẻ'].sum())
        tot_on = int(df_out['Nhóm KH Kênh ON'].sum())
        tot_vs = int(df_out['Lịch Viếng Thăm Hôm Nay'].sum())
        
        total_row = pd.DataFrame([{
            'STT': '-',
            'Mã NVBH': 'TỔNG CỘNG',
            'Tên NVBH': 'SS Trương Thanh Tân Total' if filter_nv == "Tất cả ĐDKD" else filter_nv,
            'Nhóm KH VIP3': tot_v3,
            'Nhóm KH VIP5': tot_v5,
            'Nhóm KH VIPSI': tot_vsi,
            'Nhóm KH CH Lẻ': tot_chl,
            'Nhóm KH Kênh ON': tot_on,
            'Lịch Viếng Thăm Hôm Nay': tot_vs
        }])
        df_out = pd.concat([df_out, total_row], ignore_index=True)
        
    return df_out, "10. BÁO CÁO LỊCH VIẾNG THĂM"

# ====================== GIAO DIỆN ======================
st.markdown(f"""
<div class="main-header">
    <div class="logo">{logo_svg}</div>
    <div class="title-block">
        <h1>SƯ ĐOÀN HCM4 - TRUNG ĐOÀN 10</h1>
        <h2>TRACKING KPI ĐDKD - TEAM SS TRƯƠNG THANH TÂN</h2>
    </div>
</div>
""", unsafe_allow_html=True)

col_reload, col_empty = st.columns([2, 5])
with col_reload:
    if st.button("🔄 Xóa Cache & Reload Dữ Liệu"):
        st.cache_data.clear()
        st.rerun()

with st.spinner("Đang tải dữ liệu hệ thống..."):
    df, mcp = load_main_data()
    targets = get_targets()

nv_list = sorted(mcp[find_col(mcp, ['SM name', 'SM Name', 'Tên NVBH', 'Nhân viên'])].dropna().unique().tolist()) if not mcp.empty else []

vn_time = dt.datetime.utcnow() + dt.timedelta(hours=7)
default_date = (vn_time - timedelta(days=1)).date()

# Bộ lọc chính
f1, f2, f3 = st.columns([1, 1, 1.3])
with f1:
    st.markdown('<p class="filter-label">MONTH</p>', unsafe_allow_html=True)
    st.selectbox("", ["Tháng 09/2026"], key="month", label_visibility="collapsed")
with f2:
    st.markdown('<p class="filter-label">NGÀY BÁO CÁO</p>', unsafe_allow_html=True)
    report_date = st.date_input("", value=default_date, key="ngay", label_visibility="collapsed")
with f3:
    st.markdown('<p class="filter-label">BÁO CÁO CHỌN</p>', unsafe_allow_html=True)
    kpi_map = {
        "10. BÁO CÁO LỊCH VIẾNG THĂM": "VISIT_SCHEDULE",
        "1. ASO FOCUS CHANTÉ": "CHANTE",
        "2. ASO FOCUS OMC TRỘN": "OMACHI",
        "3. ASO TEA KÊNH ON": "ASO_TEA",
        "4. PC BT (PC 4LINE - BEER)": "PC_BT",
        "5. ASO ALL": "ASO_ALL",
        "6. ASO ACTIVE KÊNH ON": "PC_ON",
    }
    selected_name = st.selectbox("", list(kpi_map.keys()), key="kpi", label_visibility="collapsed")
    selected_kpi = kpi_map[selected_name]

f4, f5 = st.columns([1, 1])
with f4:
    st.markdown('<p class="filter-label">SALE SUP</p>', unsafe_allow_html=True)
    st.selectbox("", ["Trương Thanh Tân Total"], key="sup", label_visibility="collapsed")
with f5:
    st.markdown('<p class="filter-label">ĐDKD (Nhân viên)</p>', unsafe_allow_html=True)
    filter_nv = st.selectbox("", ["Tất cả ĐDKD"] + nv_list, key="ddkd", label_visibility="collapsed")

st.markdown("---")

tab_kpi, tab_mcp = st.tabs(["📊 BÁO CÁO CHÍNH", "🗺️ MCP VISIT & DỮ LIỆU GỐC"])

with tab_kpi:
    if selected_kpi == "VISIT_SCHEDULE":
        df_visit, title = build_visit_schedule_report(mcp, report_date, filter_nv)
        tot_row = df_visit.iloc[-1] if not df_visit.empty else {}
        total_visits = int(tot_row.get('Lịch Viếng Thăm Hôm Nay', 0))
        tot_vip3 = int(tot_row.get('Nhóm KH VIP3', 0))
        tot_vip5 = int(tot_row.get('Nhóm KH VIP5', 0))
        tot_on = int(tot_row.get('Nhóm KH Kênh ON', 0))
        
        iso_wk = report_date.isocalendar()[1]
        wday_str = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7', 'Chủ Nhật'][report_date.weekday()]
        
        st.markdown(f'<h3 style="color: #034ea2; font-weight: 800; margin-bottom: 0px; font-size: 15px;">{title} - {wday_str}, NGÀY {report_date.strftime("%d/%m/%Y")} (Tuần ISO: {iso_wk} - {"Lẻ" if iso_wk%2!=0 else "Chẵn"})</h3>', unsafe_allow_html=True)
        st.caption(f"⚡ Tối ưu mô hình vận hành: Lọc chuẩn Thứ & Tuần ISO từ file Data_MCP.xlsx")
        
        c1, c2, c3, c4 = st.columns(4)
        with c1: render_metric_card("📌 Tổng Lịch Viếng Thăm", f"{total_visits:,} CH")
        with c2: render_metric_card("⭐ Tổng KH VIP (3/5/SI)", f"{tot_vip3 + tot_vip5 + int(tot_row.get('Nhóm KH VIPSI',0)):,} CH")
        with c3: render_metric_card("🏠 Tổng KH CH Lẻ", f"{int(tot_row.get('Nhóm KH CH Lẻ', 0)):,} CH")
        with c4: render_metric_card("🍻 Tổng KH Kênh ON", f"{tot_on:,} CH")
        
        st.markdown(render_html_table(df_visit), unsafe_allow_html=True)
        st.markdown(f"""
        <div class="note-box">
            <b>NHẬN XÉT & HƯỚNG DẪN BÁO CÁO LỊCH VIẾNG THĂM:</b><br>
            • Tổng số lượng cửa hàng cần viếng thăm trong ngày: <b>{total_visits:,} cửa hàng</b>.<br>
            • Phân loại chuẩn 5 nhóm loại trừ lẫn nhau: <b>VIP3, VIP5, VIPSI, CH Lẻ, Kênh ON</b>.<br>
            • Hệ thống đã tự động sắp xếp danh sách ĐDKD theo số lượng lịch viếng thăm giảm dần.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Bro chọn mục '10. BÁO CÁO LỊCH VIẾNG THĂM' ở bộ lọc KPI Name để xem kết quả chi tiết nhé!")

with tab_mcp:
    st.markdown('<h3 style="color: #034ea2; font-weight: 800; margin-bottom: 0px; font-size: 15px;">🗺️ DỮ LIỆU GỐC MCP</h3>', unsafe_allow_html=True)
    if not mcp.empty:
        st.dataframe(mcp.head(100), use_container_width=True, height=450)
    else:
        st.warning("Chưa có file Data_MCP.xlsx trong thư mục data.")
