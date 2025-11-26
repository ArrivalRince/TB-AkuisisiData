import streamlit as st
import pandas as pd

st.title("Input Dataset BANSOS PANGAN")

uploaded = st.file_uploader("Upload dataset (Excel/CSV)", type=["xlsx", "csv"])

if uploaded:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)

    st.success("Dataset berhasil diupload!")
    st.dataframe(df, use_container_width=True)

    # Simpan ke folder data
    df.to_csv("data/dataset.csv", index=False)
    st.info("Dataset disimpan ke folder data/dataset.csv")
