import streamlit as st
import pandas as pd
import random

"AIzaSyBK0GEKUzpn93pl4DpgADH1HhQxklm1mX0"
rc = pd.read_csv("data.csv")
ert = st.write(rc)
x = st.slider("Select a value")
st.write(x, "squared is", x * x)
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
df = pd.DataFrame([random.random(), title, 3, 4, 5, 6, 7])
df.to_csv("data.csv")
rc = pd.read_csv("data.csv")
st.write(rc)
