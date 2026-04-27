import streamlit as st

# --- 網頁基本設定 ---
st.set_page_config(
    page_title="酸鹼鹽究院｜理化互動複習站",
    page_icon="🧪",
    layout="wide"
)

# --- 自定義 CSS 樣式 ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #f0f2f6;
        border-radius: 5px 5px 0px 0px;
        gap: 1px;
        padding-left: 20px;
        padding-right: 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 側邊導航欄 ---
with st.sidebar:
    st.title("🐍 導航選單")
    chapter = st.radio(
        "選擇複習章節：",
        ["🏠 網站首頁", "🍋 CH3 酸、鹼、鹽", "🔥 CH4 反應速率與平衡"]
    )
    st.divider()
    st.caption("2026 段考衝刺專用版本")

# --- 1. 網站首頁 ---
if chapter == "🏠 網站首頁":
    st.title("🧪 酸鹼鹽究院")
    st.subheader("用程式碼征服理化段考！")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        ### 📖 本站複習指南
        歡迎來到**酸鹼鹽究院**！這裡專為國中理化第四冊精心打造：
        - **互動實驗**：不用進實驗室也能看顏色變化。
        - **重點歸納**：幫你整理好最愛考的魔鬼細節。
        - **即時測驗**：滑滑選單，立刻檢查觀念是否正確。
        
        **準備好就從左側選單開始吧！**
        """)
        if st.button("🎉 點我領取段考好運"):
            st.balloons()
            st.success("好運加持成功！考的都會，猜的都對！")
    
    with col2:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJndzZ4dzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9iZW5kZXImY3Q9Zw/l41lTfuxV5F6F0TDi/giphy.gif", caption="理化學習中...")

# --- 2. CH3 酸、鹼、鹽 ---
elif chapter == "🍋 CH3 酸、鹼、鹽":
    st.title("🍋 第 3 章：酸、鹼、鹽")
    st.write("本章核心：了解離子如何導電，以及酸鹼中和的反應。")

    # 使用 Tabs 分隔小節
    tab1, tab2, tab3, tab4 = st.tabs(["3-1 電解質", "3-2 常見酸鹼", "3-3 濃度與 pH 值", "3-4 酸鹼中和"])

    # --- 3-1 電解質 ---
    with tab1:
        st.subheader("💡 電解質與解離")
        st.info("電解質：溶於水能導電的化合物（必須產生自由移動的離子）。")
        
        # 互動小實驗
        test_sub = st.selectbox("🧪 把物質放入水中測導電性：", ["請選擇...", "食鹽 (NaCl)", "酒精 (C2H5OH)", "氫氧化鈉 (NaOH)", "蔗糖"])
        if test_sub == "食鹽 (NaCl)":
            st.success("✅ 強電解質：燈泡發亮！ $NaCl \\rightarrow Na^+ + Cl^-$")
        elif test_sub == "氫氧化鈉 (NaOH)":
            st.success("✅ 強電解質：燈泡發亮！ $NaOH \\rightarrow Na^+ + OH^-$")
        elif test_sub == "酒精 (C2H5OH)" or test_sub == "蔗糖":
            st.error("❌ 非電解質：燈泡不亮。分子在水中不解離。")

    # --- 3-2 常見酸鹼 ---
    with tab2:
        st.subheader("🧼 常見酸鹼圖鑑")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown("### **常見的酸**")
            st.write("- **硫酸 ($H_2SO_4$):** 脫水性、稀釋需將酸加入水。")
            st.write("- **硝酸 ($HNO_3$):** 照光變褐、與銅產生紅棕色 $NO_2$。")
            st.write("- **鹽酸 ($HCl$):** 具揮發性、胃酸成分。")
        with col_b:
            st.markdown("### **常見的鹼**")
            st.write("- **氫氧化鈉 ($NaOH$):** 燒鹼、苛性鈉，可除油污。")
            st.write("- **氨 ($NH_3$):** 具刺鼻味，易溶於水。")
            st.write("- **氫氧化鈣 ($Ca(OH)_2$):** 澄清石灰水，檢驗 $CO_2$。")

    # --- 3-3 濃度與 pH 值 ---
    with tab3:
        st.subheader("🌈 pH 值變色模擬器")
        ph = st.slider("調整 pH 值，看廣用試劑的顏色變化：", 0, 14, 7)
        
        # 根據 pH 值決定顯示顏色
        if ph <= 2: color_hex, tag = "#FF0000", "強酸 (紅)"
        elif ph <= 4: color_hex, tag = "#FF7F00", "酸 (橙)"
        elif ph <= 6: color_hex, tag = "#FFFF00", "弱酸 (黃)"
        elif ph == 7: color_hex, tag = "#00FF00", "中性 (綠)"
        elif ph <= 9: color_hex, tag = "#0000FF", "弱鹼 (藍)"
        elif ph <= 11: color_hex, tag = "#4B0082", "鹼 (靛)"
        else: color_hex, tag = "#8B00FF", "強鹼 (紫)"
        
        st.markdown(f"""
            <div style="background-color:{color_hex}; padding:30px; border-radius:15px; text-align:center;">
                <h1 style="color:white; margin:0;">pH = {ph}</h1>
                <h3 style="color:white; margin:0;">{tag}</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("---")
        st.latex(r"M = \frac{n}{V} \text{ (莫耳/公升)}")

    # --- 3-4 酸鹼中和 ---
    with tab4:
        st.subheader("🧪 酸鹼中和與鹽類")
        st.warning("核心公式：$酸 + 鹼 \rightarrow 鹽 + 水 + 熱$")
        
        with st.expander("📝 必背鹽類重點"):
            st.write("1. **氯化鈉 (NaCl)**：食鹽，最常見的鹽類。")
            st.write("2. **碳酸鈣 (CaCO3)**：大理石、貝殼，不溶於水。")
            st.write("3. **碳酸氫鈉 (NaHCO3)**：小蘇打，加熱產生 $CO_2$，用於烘焙。")
            st.write("4. **硫酸鈣 (CaSO4)**：石膏的主要成分。")

# --- 3. CH4 (預留位置) ---
elif chapter == "🔥 CH4 反應速率與平衡":
    st.title("🔥 CH4 反應速率與平衡")
    st.write("這章節正在實驗室開發中... 敬請期待！")
