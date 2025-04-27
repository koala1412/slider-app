import streamlit as st

# ガラス感のCSSとスライダーを太くするCSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, rgba(255,255,255,0.2), rgba(255,255,255,0.1));
        backdrop-filter: blur(12px);
        height: 100vh;
        font-family: 'Roboto', sans-serif;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.25);
        border-radius: 20px;
        padding: 40px;
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    .stSlider > div[data-baseweb="slider"] {
        height: 30px; /* スライダーを太くする */
    }
    footer {
        visibility: hidden;
    }
    .custom-footer {
        position: fixed;
        bottom: 10px;
        right: 20px;
        color: #ccc;
        font-size: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# メインコンテンツ
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.title("🌟 わくわくメーター 🌟")
st.write("スライダーを動かしてわくわく度をチェックしよう！")

# スライダーだけ！
value = st.slider('数値を選択', 0, 100, 50)

# 数値によって色をもっと自然にグラデ
# 0(青) → 50(紫) → 100(赤)
def get_color(v):
    if v < 50:
        # 0~50 青(0,0,255) → 紫(128,0,128)
        ratio = v / 50
        r = int(128 * ratio)
        g = 0
        b = int(255 - (127 * ratio))
    else:
        # 50~100 紫(128,0,128) → 赤(255,0,0)
        ratio = (v - 50) / 50
        r = int(128 + (127 * ratio))
        g = 0
        b = int(128 - (128 * ratio))
    return f"rgb({r},{g},{b})"

color = get_color(value)

# わくわく度をカラフルに表示
st.markdown(
    f"<h2 style='text-align:center; color: {color}; font-size: 48px;'>🎯 現在のわくわく度： {int(value)} / 100</h2>",
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)