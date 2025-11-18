import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D

st.title("📊 Data Visualization Dashboard")

# Cek session_state
if "cluster_data" not in st.session_state:
    st.warning("⚠️ Lakukan analisis clustering terlebih dahulu!")
    st.stop()

data = st.session_state["cluster_data"]

# Cek cluster
if "Cluster" not in data.columns:
    st.error("❌ Hasil clustering belum tersedia.")
    st.stop()

numeric_cols = data.select_dtypes(include=['float', 'int']).columns

if len(numeric_cols) < 2:
    st.error("Minimal butuh 2 kolom numerik.")
    st.stop()

# ===============================
# 1. Scatter Plot (2 variabel)
# ===============================
st.subheader("📌 Scatter Plot (2 Variabel)")

x_col = st.selectbox("Pilih kolom X", numeric_cols, index=0)
y_col = st.selectbox("Pilih kolom Y", numeric_cols, index=1)

fig, ax = plt.subplots()
scatter = ax.scatter(data[x_col], data[y_col], c=data["Cluster"], cmap="tab10")
ax.set_xlabel(x_col)
ax.set_ylabel(y_col)
ax.set_title("Scatter Plot Berdasarkan Cluster")
ax.legend(*scatter.legend_elements(), title="Cluster")
st.pyplot(fig)

# ===============================
# 2. Scatter Matrix (Pairplot Manual)
# ===============================
st.subheader("📌 Pairplot Sederhana (Scatter Matrix)")

selected_cols = st.multiselect("Pilih kolom untuk Pairplot", numeric_cols, default=numeric_cols[:3])

if len(selected_cols) > 1:
    fig, axes = plt.subplots(len(selected_cols), len(selected_cols), figsize=(12, 12))

    for i in range(len(selected_cols)):
        for j in range(len(selected_cols)):
            if i == j:
                axes[i, j].hist(data[selected_cols[i]])
                axes[i, j].set_title(f"{selected_cols[i]}")
            else:
                axes[i, j].scatter(data[selected_cols[j]], data[selected_cols[i]],
                                   c=data["Cluster"], cmap="tab10", s=5)
    st.pyplot(fig)

# ===============================
# 3. Heatmap Korelasi
# ===============================
st.subheader("📌 Heatmap Korelasi Fitur")

corr = data[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
heatmap = ax.imshow(corr, cmap="coolwarm")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=45)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.colorbar(heatmap)
st.pyplot(fig)

# ===============================
# 4. Jumlah Data per Cluster (Bar Chart)
# ===============================
st.subheader("📌 Jumlah Data per Cluster")

cluster_count = data["Cluster"].value_counts().sort_index()

fig, ax = plt.subplots()
ax.bar(cluster_count.index, cluster_count.values)
ax.set_xlabel("Cluster")
ax.set_ylabel("Jumlah Data")
ax.set_title("Jumlah Data per Cluster")
st.pyplot(fig)

# ===============================
# 5. 3D Scatter Plot
# ===============================
if len(numeric_cols) >= 3:
    st.subheader("📌 3D Scatter Plot")

    x3 = st.selectbox("X (3D)", numeric_cols, index=0, key="x3")
    y3 = st.selectbox("Y (3D)", numeric_cols, index=1, key="y3")
    z3 = st.selectbox("Z (3D)", numeric_cols, index=2, key="z3")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    img = ax.scatter(data[x3], data[y3], data[z3], c=data["Cluster"], cmap="tab10")
    ax.set_xlabel(x3)
    ax.set_ylabel(y3)
    ax.set_zlabel(z3)
    ax.set_title("3D Scatter Plot")
    st.pyplot(fig)

# ===============================
# 6. Boxplot per Fitur per Cluster
# ===============================
st.subheader("📌 Boxplot Fitur Berdasarkan Cluster")

feat = st.selectbox("Pilih fitur", numeric_cols)

fig, ax = plt.subplots()
data.boxplot(column=feat, by="Cluster", ax=ax)
ax.set_title(f"Boxplot {feat} per Cluster")
ax.set_xlabel("Cluster")
ax.set_ylabel(feat)
plt.suptitle("")
st.pyplot(fig)
