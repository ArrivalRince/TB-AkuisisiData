import streamlit as st
import pandas as pd

st.title("Input Dataset Bantuan Sosial Pangan")

# upload file
uploaded = st.file_uploader("Dataset ini akan digunakan untuk proses **Preprocessing, Analysis, dan Visualisasi** pada tahap berikutnya.", 
                            type=["csv", "xlsx"])

# proses file yang diupload
if uploaded:

    # Deteksi format file
    try:
        if uploaded.name.endswith(".csv"):
            df = pd.read_csv(uploaded)
        else:
            df = pd.read_excel(uploaded)

        st.success("✔ Dataset berhasil diunggah!")
        
        # Tampilkan 5 baris pertama
        st.subheader("Preview Dataset")
        st.dataframe(df, use_container_width=True)

        # Simpan dataset ke folder data
        try:
            df.to_csv("data/dataset.csv", index=False)
            st.info("")
        except:
            st.warning("")

        # Informasi jumlah baris & kolom
        st.subheader("Informasi Dataset")
        col1, col2, col3 = st.columns(3)
        col1.metric("Jumlah Baris", df.shape[0])
        col2.metric("Jumlah Kolom", df.shape[1])
        col3.metric("Status", "Siap diproses")

        # Penjelasan tambahan
        st.write("""
        **Catatan:**  
        Pastikan dataset memiliki kolom seperti:
        - *Provinsi*  
        - *Realisasi_Jumlah_KPM*  
        - *Realisasi_Anggaran*  
        
        karena kolom-kolom tersebut akan digunakan pada tahap **Analisis** dan **Visualisasi**.
        """)

    except Exception as e:
        st.error(f"Terjadi kesalahan dalam membaca file: {e}")

else:
    st.info("⬆ Silakan unggah dataset terlebih dahulu untuk mulai proses analisis.")
