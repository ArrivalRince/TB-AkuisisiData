import streamlit as st
import pandas as pd

st.title("🧹 Preprocessing Data")

# Pastikan dataset sudah diupload
if "raw_data" not in st.session_state:
    st.warning("Silakan upload dataset terlebih dahulu di menu *Input Data*.")
else:
    df = st.session_state["raw_data"]

    st.subheader("📊 Statistik Sebelum Preprocessing")
    st.write(df.describe(include="all"))
    st.write("Jumlah data:", len(df))
    st.write("Jumlah nilai kosong per kolom:")
    st.write(df.isnull().sum())

    st.markdown("---")

    # ---------------------------
    # HAPUS DUPLIKAT
    # ---------------------------
    st.subheader("🧽 Menghapus Data Duplikat")

    duplicates = df.duplicated().sum()
    st.write("Jumlah data duplikat:", duplicates)

    if st.button("Hapus Duplikat"):
        df = df.drop_duplicates()
        st.success(f"{duplicates} data duplikat berhasil dihapus!")

    st.markdown("---")

    # ---------------------------
    # HANDLE MISSING VALUES
    # ---------------------------
    st.subheader("🩹 Mengatasi Nilai Kosong")

    method = st.radio(
        "Pilih metode penanganan missing value:",
        ["Hapus baris yang memiliki NaN", "Isi dengan Mean", "Isi dengan Median", "Isi dengan Mode"]
    )

    if st.button("Proses Missing Value"):
        if method == "Hapus baris yang memiliki NaN":
            df = df.dropna()
            st.success("Baris yang memiliki NaN berhasil dihapus!")

        elif method == "Isi dengan Mean":
            df = df.fillna(df.mean(numeric_only=True))
            st.success("Missing value berhasil diisi dengan Mean!")

        elif method == "Isi dengan Median":
            df = df.fillna(df.median(numeric_only=True))
            st.success("Missing value berhasil diisi dengan Median!")

        elif method == "Isi dengan Mode":
            df = df.fillna(df.mode().iloc[0])
            st.success("Missing value berhasil diisi dengan Mode!")

    st.markdown("---")

    # ---------------------------
    # STATISTIK SETELAH PREPROCESSING
    # ---------------------------
    st.subheader("📊 Statistik Setelah Preprocessing")
    st.write(df.describe(include="all"))
    st.write("Jumlah data:", len(df))
    st.write("Jumlah nilai kosong per kolom:")
    st.write(df.isnull().sum())

    # Simpan hasil preprocessing ke session state
    st.session_state["clean_data"] = df
