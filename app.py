import streamlit as st

# --- 網頁配置 ---
st.set_page_config(page_title="酸鹼鹽究院", page_icon="🧪", layout="wide")

# --- 1. 定義導航狀態 ---
# 使用 session_state 來追蹤使用者目前在哪個「大頁面」
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def go_to(page_name):
    st.session_state.page = page_name

# --- 側邊欄：始終存在的快速跳轉 ---
st.sidebar.title("🧬 選單")
if st.sidebar.button("🏠 回首頁"):
    go_to('home')
if st.sidebar.button("🍋 第三章：酸鹼鹽"):
    go_to('ch3')
if st.sidebar.button("🔥 第四章：反應速率"):
    go_to('ch4')

st.sidebar.divider()
st.sidebar.caption("2026 理化段考複習系統 v1.0")

# --- 2. 頁面邏輯 ---

# === A. 首頁 (Home) ===
if st.session_state.page == 'home':
    st.title("🧪 酸鹼鹽究院｜首頁")
    st.subheader("用 Python 打造的理化複習神器")
    
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        st.info("### 🍋 第三章：酸、鹼、鹽")
        st.write("探索電解質、酸鹼性質、濃度計算與酸鹼中和。")
        if st.button("進入第三章複習 ➔"):
            go_to('ch3')
            st.rerun()

    with col2:
        st.warning("### 🔥 第四章：反應速率與平衡")
        st.write("理解反應快慢的因素，以及勒沙特列原理的奧秘。")
        if st.button("進入第四章複習 ➔"):
            go_to('ch4')
            st.rerun()
    st.markdown("---")

# === B. 第三章分頁 (CH3) ===
elif st.session_state.page == 'ch3':
    st.title("🍋 第 3 章：酸、鹼、鹽")
    st.write("請選擇下方的小章節進行複習：")

    # 利用 Tabs 實現「分頁連結到多個小章節」
    ch3_tabs = st.tabs(["3-1 電解質", "3-2 常見酸鹼", "3-3 濃度與 pH 值", "3-4 酸鹼中和"])

    with ch3_tabs[0]:
        st.subheader("3-1 電解質與解離")
        st.write("💡 重點：溶於水能導電的化合物稱為電解質。")
        # 這裡可以放你的互動小實驗...

    with ch3_tabs[1]:
        st.subheader("3-2 常見酸鹼圖鑑")
        st.write("💡 重點：硫酸、鹽酸、硝酸、氫氧化鈉、氨、氫氧化鈣。")

    with ch3_tabs[2]:
        st.subheader("3-3 濃度與 pH 值")
        st.write("💡 重點：莫耳濃度 $M$ 與廣用試劑顏色變化。")
        # pH 值滑桿可以放在這

    with ch3_tabs[3]:
        st.subheader("3-4 酸鹼中和與鹽類")
        st.write("💡 重點：$酸 + 鹼 \rightarrow 鹽 + 水 + 熱$。")

# === C. 第四章分頁 (CH4) ===
elif st.session_state.page == 'ch4':
    st.title("🔥 第 4 章：反應速率與平衡")
    st.write("請選擇下方的小章節進行複習：")

    ch4_tabs = st.tabs(["4-1 反應速率", "4-2 化學平衡"])

    with ch4_tabs[0]:
        st.subheader("4-1 反應速率")
        st.write("💡 重點：影響反應快慢的五大因素（溫度、濃度、表面積、催化劑、本性）。")

    with ch4_tabs[1]:
        st.subheader("4-2 化學平衡")
        st.write("💡 重點：勒沙特列原理 —— 改變壓力、濃度或溫度時的平衡移動。")

# --- 頁尾 ---
st.divider()
if st.session_state.page != 'home':
    if st.button("⬅ 返回首頁"):
        go_to('home')
        st.rerun()
