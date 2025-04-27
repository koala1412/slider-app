import streamlit as st

st.title("スライダーでバーを動かすアプリ")

# スライダー
value = st.slider('数値を選んでね', 0, 100, 50)

# 棒グラフ（みたいなやつ）
st.write("現在の値:", value)
st.progress(value)
