import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Styling CSS
st.markdown("""
<style>
body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(to bottom, #eef2f3, #8e9eab);
}
header {
    background-color: #6a11cb;
    color: white;
    text-align: center;
    padding: 10px 0;
    border-radius: 10px;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown("<header><h2>Analisis Bantuan Sosial dan Tingkat Kesejahteraan Daerah</h2></header>", unsafe_allow_html=True)

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        menu_title="Navigasi",
        options=["Home", "Input Data", "Preprocessing", "Analysis", "Visualizations", "About Us"],
        icons=["house", "upload", "gear", "bar-chart", "graph-up", "info-circle"],
        default_index=0
    )

# Save data session
if "data" not in st.session_state:
    st.session_state["data"] = None

# HOME
def home():
    st.header("Selamat Datang")
    st.write("""
    Aplikasi ini digunakan untuk menganalisis hubungan antara **bantuan sosial dan tingkat kesejahteraan daerah (Provinsi)**.
    
    Anda dapat:
    - Mengunggah dataset provinsi
    - Melakukan preprocessing
    - Melakukan analisis statistik
    - Melihat visualisasi hubungan antar variabel
    """)

# INPUT DATA
def input_data():
    st.header("Input Data")
    uploaded_file = st.file_uploader("Unggah dataset CSV (wajib berisi kolom: Provinsi, Tingkat_Kesejahteraan)", type=["csv"])
    
    if uploaded_file:
        try:
            data = pd.read_csv(uploaded_file)
            st.session_state["data"] = data
            st.success("Dataset berhasil diunggah!")
            st.dataframe(data)
        except:
            st.error("Format file tidak valid. Pastikan file berupa CSV.")

# PREPROCESSING
def preprocessing():
    st.header("Preprocessing Data")
    if st.session_state["data"] is None:
        st.warning("Harap unggah data terlebih dahulu.")
        return

    data = st.session_state["data"]

    st.subheader("Data Sebelum Preprocessing")
    st.dataframe(data)

    # Drop duplicates
    data = data.drop_duplicates()

    # Handle missing values
    for col in data.columns:
        if data[col].dtype in ["float64", "int64"]:
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)

    # Convert to numeric if needed
    if "Tingkat_Kesejahteraan" in data.columns:
        data["Tingkat_Kesejahteraan"] = pd.to_numeric(data["Tingkat_Kesejahteraan"], errors="coerce")
        data.dropna(subset=["Tingkat_Kesejahteraan"], inplace=True)

    st.subheader("Data Setelah Preprocessing")
    st.dataframe(data)

    st.session_state["data"] = data
    st.success("Preprocessing selesai!")

# ANALYSIS
def analysis():
    st.header("Analisis Data")
    if st.session_state["data"] is None:
        st.warning("Harap unggah atau proses data terlebih dahulu.")
        return

    data = st.session_state["data"]

    st.subheader("Statistik Tingkat Kesejahteraan")
    st.write(data["Tingkat_Kesejahteraan"].describe())

    bantuan_cols = [col for col in data.columns if "Bantuan" in col]
    
    if bantuan_cols:
        st.subheader("Rata-rata Bantuan Sosial per Provinsi")
        st.dataframe(data.groupby("Provinsi")[bantuan_cols].mean())

        st.subheader("Korelasi Bantuan Sosial dengan Kesejahteraan")
        corr = data[bantuan_cols + ["Tingkat_Kesejahteraan"]].corr()
        st.write(corr)
    else:
        st.info("Tidak ditemukan kolom bantuan sosial di dataset.")

# VISUALIZATIONS
def visualizations():
    st.header("Visualisasi Data")
    if st.session_state["data"] is None:
        st.warning("Harap unggah data terlebih dahulu.")
        return

    data = st.session_state["data"]

    # 1. Scatter plot Provinsi vs Tingkat Kesejahteraan
    st.subheader("Scatter Plot Provinsi vs Tingkat Kesejahteraan")

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.scatterplot(x="Provinsi", y="Tingkat_Kesejahteraan", data=data, s=120)
    plt.xticks(rotation=90)
    ax.set_title("Kesejahteraan per Provinsi")
    ax.set_ylabel("Tingkat Kesejahteraan")
    st.pyplot(fig)

    bantuan_cols = [col for col in data.columns if "Bantuan" in col]

    # 2. Korelasi heatmap
    if bantuan_cols:
        st.subheader("Heatmap Korelasi Bantuan Sosial dan Kesejahteraan")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(data[bantuan_cols + ["Tingkat_Kesejahteraan"]].corr(), annot=True, cmap="coolwarm")
        st.pyplot(fig)

    # 3. Clustering (optional)
    if bantuan_cols:
        st.subheader("Clustering Berdasarkan Bantuan Sosial")
        features = bantuan_cols + ["Tingkat_Kesejahteraan"]

        scaler = StandardScaler()
        scaled = scaler.fit_transform(data[features])

        kmeans = KMeans(n_clusters=3, random_state=42)
        data["Cluster"] = kmeans.fit_predict(scaled)

        fig, ax = plt.subplots(figsize=(10, 5))
        sns.scatterplot(x="Tingkat_Kesejahteraan", y=bantuan_cols[0], data=data, hue="Cluster", palette="tab10")
        ax.set_title("Clustering Provinsi Berdasarkan Bantuan Sosial")
        st.pyplot(fig)

# ABOUT US
def about_us():
    st.header("Tentang Kami")
    st.write("""
    Aplikasi ini dikembangkan oleh Kelompok 5 Mata Kuliah Akuisisi Data.  
    Fokus aplikasi ini adalah **analisis pemerataan bantuan sosial terhadap kesejahteraan provinsi di Indonesia**.
    """)

# ROUTER
if selected == "Home":
    home()
elif selected == "Input Data":
    input_data()
elif selected == "Preprocessing":
    preprocessing()
elif selected == "Analysis":
    analysis()
elif selected == "Visualizations":
    visualizations()
elif selected == "About Us":
    about_us()
