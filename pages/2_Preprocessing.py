import streamlit as st
import pandas as pd

st.title("Preprocessing Data BANSOS PANGAN")

# Load dataset
try:
    df = pd.read_csv("data/dataset.csv")
except:
    st.error("Dataset belum diupload. Silakan upload di menu Input Data.")
    st.stop()

st.subheader("Data Sebelum Preprocessing")
st.dataframe(df, use_container_width=True)

# 1. Membersihkan baris tidak valid
st.subheader("Menghapus Baris Tidak Valid (Indonesia, 0, Catatan, BPNT)")

invalid_keywords = ["Indonesia", "0", "Catatan", "Bantuan Pangan Non-Tunai (BPNT)"]

before_rows = df.shape[0]

df = df[~df["Provinsi"].isin(invalid_keywords)]

after_rows = df.shape[0]

st.success(f"Baris dihapus: {before_rows - after_rows} baris")
st.dataframe(df, use_container_width=True)


# 2. Cek nilai kosong (NA)
st.subheader(" Deteksi Nilai Kosong (NA)")

na_info = df.isna().sum()

st.write(na_info)

if na_info.sum() == 0:
    st.info("Tidak ada nilai kosong dalam dataset.")
else:
    st.warning("Dataset memiliki nilai kosong.")

# 3. Opsi Penanganan Nilai Kosong

st.subheader("Pilih Metode Penanganan NA")

option = st.radio(
    "Pilih metode:",
    [
        "Isi nilai NA dengan MEAN",
        "Isi nilai NA dengan 0",
        "Hapus baris yang memiliki NA"
    ]
)

df_clean = df.copy()

if option == "Isi nilai NA dengan MEAN":
    numeric_cols = df_clean.select_dtypes(include=["float64", "int64"]).columns
    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(df_clean[numeric_cols].mean())
    st.success("Nilai NA telah diisi dengan MEAN.")

elif option == "Isi nilai NA dengan 0":
    df_clean = df_clean.fillna(0)
    st.success("Nilai NA telah diisi dengan 0.")

elif option == "Hapus baris yang memiliki NA":
    df_clean = df_clean.dropna()
    st.success("Baris berisi NA telah dihapus seluruhnya.")


# 4. Rename kolom panjang  
df_clean.rename(columns={
    "Rencana Jumlah Keluarga Penerima Manfaat (KPM) Bantuan Sosial Pangan (BANSOS PANGAN)": "Rencana_Jumlah_KPM",
    "Realisasi Jumlah Keluarga Penerima Manfaat (KPM) Bantuan Sosial Pangan (BANSOS PANGAN)": "Realisasi_Jumlah_KPM",
    "Rencana Anggaran Bantuan Sosial Pangan (BANSOS PANGAN) (Rp)": "Rencana_Anggaran",
    "Realisasi Anggaran Bantuan Sosial Pangan (BANSOS PANGAN) (Rp)": "Realisasi_Anggaran"
}, inplace=True)

# 5. Hasil Akhir

st.subheader("Data Setelah Preprocessing")
st.dataframe(df_clean, use_container_width=True)

# Simpan hasil preprocessing ke CSV
df_clean.to_csv("data/clean_dataset.csv", index=False)

# SIMPAN KE SESSION STATE AGAR BISA DIBACA HALAMAN ANALYSIS
st.session_state["data"] = df_clean

st.success("Preprocessing selesai! Data disimpan dan siap dianalisis.")

