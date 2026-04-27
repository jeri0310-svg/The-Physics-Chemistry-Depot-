import streamlit as st

# 設定網頁標題與圖示
st.set_page_config(page_title="理化段考大作戰", page_icon="🧪", layout="wide")

# 自定義 CSS 讓介面更有趣
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 首頁標題 ---
st.title("🧪 理化段考複習補給站")
st.subheader("範圍：第四冊 CH3 酸鹼鹽 ＆ CH4 反應速率與平衡")
st.info("💡 這裡不只有筆記，還有能讓你玩到背起來的互動工具！")

# --- 側邊欄導航 ---
st.sidebar.title("章節選單")
chapter = st.sidebar.radio("選擇你想複習的章節：", ["首頁總覽", "CH3 酸鹼鹽", "CH4 反應速率與平衡"])

if chapter == "首頁總覽":
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏆 段考必殺技")
        st.write("- **口訣記憶法：** 實驗步驟、顏色變化。")
        st.write("- **互動模擬：** 看看 pH 值怎麼變。")
        st.write("- **迷因重點：** 那些老師愛考的陷阱題。")
        
    with col2:
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJndzZ4dzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4ZzB4JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZAmN0PWc/3o7TKMGpxU8EsaS5m8/giphy.gif", caption="理化實驗真的很好玩（只要不炸掉）")

    st.divider()
    
    # 快速挑戰區
    st.markdown("### ⚡️ 快速暖身題")
    q1 = st.radio("下列哪一個不是電解質？", ["食鹽", "酒精", "氫氧化鈉"])
    if st.button("檢查答案"):
        if q1 == "酒精":
            st.success("正確！酒精是中性分子，不解離。")
        else:
            st.error("答錯了！食鹽和強鹼都是電解質喔。")

elif chapter == "CH3 酸鹼鹽":
    st.header("🍋 CH3 酸鹼鹽重點")
    st.markdown("#### **1. 酸鹼指示劑變色表**")
    # 這裡可以用表格呈現
    st.table({
        "指示劑": ["廣用試劑", "酚酞", "石蕊"],
        "酸性": ["紅/橙", "無色", "紅"],
        "中性": ["黃/綠", "無色", "紫色"],
        "鹼性": ["藍/紫", "粉紅", "藍"]
    })
    st.warning("⚠️ 記得：酸性加水稀釋，pH 值會上升但**絕對不會**大於 7！")

elif chapter == "CH4 反應速率與平衡":
    st.header("🔥 CH4 反應速率與平衡")
    st.markdown("#### **影響反應速率的因素**")
    factors = ["溫度", "濃度", "接觸面積", "催化劑", "物質本性"]
    selected_factor = st.selectbox("選擇一個因素看解釋：", factors)
    
    if selected_factor == "溫度":
        st.write("📈 **原理：** 溫度升高，粒子動能增加，**有效碰撞次數**變多。")
    elif selected_factor == "接觸面積":
        st.write("🧱 **原理：** 顆粒越細（如粉末），反應面積越大，速率越快。")
        
    st.info("⚖️ **勒沙特列原理：** 當平衡受到改變，系統會往『抵消改變』的方向移動。")

# --- 頁尾 ---
st.markdown("---")
st.caption("Made with ❤️ by Your Name | 2026 理化複習專案")
