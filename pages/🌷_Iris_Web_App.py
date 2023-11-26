import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Web App Iris", page_icon="🌷")

st.write("# 🌷 Klasifikasi Bunga Iris 🌷")
st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")

c1,c2 = st.columns([2,3])

with c1:
    st.image("iris_.png")

with c2:
    petal_p = st.number_input('Panjang Petal')
    petal_l = st.number_input('Lebar Petal')
    sepal_p = st.number_input('Panjang Sepal')
    sepal_l = st.number_input('Lebar Sepal')

    prediksi = st.button("Prediksi")
st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")

