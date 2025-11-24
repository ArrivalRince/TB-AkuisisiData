import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

st.title("📊 Analysis – K-Means Clustering Bantuan Sosial")

# Cek data dari preprocessing
if "data" not in st.session_state or st.session_state["data"] is None:
    st.warning("Silakan lakukan preprocessing terlebih dahulu!")
    st.stop()

df = st.session_state["data"]

st.subheader("📌 Data Siap Analisis")
st.dataframe(df, use_container_width=True)

# Kolom yang digunakan untuk clustering
kpm_col = "Realisasi_Jumlah_KPM"
anggaran_col = "Realisasi_Anggaran"

features = [kpm_col, anggaran_col]

# Pastikan kolom benar-benar ada
missing = [col for col in features if col not in df.columns]
if missing:
    st.error(f"Kolom berikut tidak ditemukan dalam dataset: {missing}")
    st.stop()

X = df[features]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method
st.subheader("📐 Penentuan Jumlah Cluster (Elbow Method)")
wcss = []
K = range(1, 10)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

fig, ax = plt.subplots()
ax.plot(K, wcss, marker="o")
ax.set_xlabel("Jumlah Cluster")
ax.set_ylabel("WCSS")
ax.set_title("Elbow Method")
st.pyplot(fig)

# Pilih jumlah cluster
n_cluster = st.slider("Pilih jumlah cluster:", 2, 8, 3)

# Jalankan clustering
kmeans = KMeans(n_clusters=n_cluster, random_state=42)
df["Cluster"] = kmeans.fit_predict(X_scaled)

# Simpan diback ke session_state
st.session_state["data"] = df

st.success("Clustering selesai!")

st.subheader("📄 Hasil Cluster")
st.dataframe(df[["Provinsi"] + features + ["Cluster"]], use_container_width=True)
