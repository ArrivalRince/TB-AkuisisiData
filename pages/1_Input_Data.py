import streamlit as st
import pandas as pd

st.title("📤 Input Data")

uploaded = st.file_uploader("Upload dataset CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    st.success("Dataset berhasil diupload!")
    st.write(df.head())

    st.session_state["raw_data"] = df
