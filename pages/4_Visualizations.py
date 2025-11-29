import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Visualizations Bantuan Sosial & Kesejahteraan")

# Cek data
if "data" not in st.session_state or st.session_state["data"] is None:
    st.warning("Silakan lakukan preprocessing dan analysis terlebih dahulu!")
    st.stop()

df = st.session_state["data"]

st.subheader(" Data yang Digunakan")
st.dataframe(df, use_container_width=True)


# 1. PERSENTASE NASIONAL

st.header("1. Persentase Kontribusi Nasional per Provinsi")

# Hitung persentase
df["Persen_KPM"] = df["Realisasi_Jumlah_KPM"] / df["Realisasi_Jumlah_KPM"].sum() * 100
df["Persen_Anggaran"] = df["Realisasi_Anggaran"] / df["Realisasi_Anggaran"].sum() * 100

#  1.1 BAR CHART PERSENTASE KPM
st.subheader("Persentase KPM per Provinsi")

fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(x="Provinsi", y="Persen_KPM", data=df, ax=ax)

ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_ylabel("Persentase (%)")
ax.set_title("Persentase Penerima Bantuan (KPM) per Provinsi")

# label jumlah KPM di atas batang
for i, row in df.iterrows():
    ax.text(
        i,
        row["Persen_KPM"] + 0.3,     
        f'{int(row["Realisasi_Jumlah_KPM"]):,}', 
        ha='center',
        fontsize=8
    )

st.pyplot(fig)


#  1.2 BAR CHART PERSENTASE ANGGARAN


st.subheader("Persentase Anggaran Bansos per Provinsi")

fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(x="Provinsi", y="Persen_Anggaran", data=df, ax=ax)

ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_ylabel("Persentase (%)")
ax.set_title("Persentase Anggaran Bantuan Sosial per Provinsi")

# label anggaran di atas batang
for i, row in df.iterrows():
    ax.text(
        i,
        row["Persen_Anggaran"] + 0.3,
        f'Rp {row["Realisasi_Anggaran"]:,.0f}',
        ha='center',
        fontsize=8
    )

st.pyplot(fig)



#  2. REALISASI VS RENCANA


st.header("2. Persentase Realisasi dibanding Rencana")

# Hitung persentase realisasi
df["Realisasi_vs_Rencana_KPM"] = (df["Realisasi_Jumlah_KPM"] / df["Rencana_Jumlah_KPM"]) * 100
df["Realisasi_vs_Rencana_Anggaran"] = (df["Realisasi_Anggaran"] / df["Rencana_Anggaran"]) * 100



# 2.1 BAR CHART REALISASI KPM (%) terhadap RENACANA

st.subheader("Persentase Realisasi KPM terhadap Rencana")

fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(x="Provinsi", y="Realisasi_vs_Rencana_KPM", data=df, ax=ax)

ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_ylabel("Persentase (%)")
ax.set_title("Persentase Realisasi Jumlah KPM terhadap Rencana")
ax.axhline(100, color="red", linestyle="--")


# label persentase di atas batang 
for p, value in zip(ax.patches, df["Realisasi_vs_Rencana_KPM"]):
    ax.text(
        p.get_x() + p.get_width() / 2,
        p.get_height() + 1,
        f"{value:.1f}%",
        ha="center",
        va="bottom",
        fontsize=8,
        rotation=0,
        fontweight="bold"
    )

st.pyplot(fig)


# 2.2 BAR CHART REALISASI ANGGARAN (%) terhadap RENCANA


st.subheader("Persentase Realisasi Anggaran terhadap Rencana")

fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(x="Provinsi", y="Realisasi_vs_Rencana_Anggaran", data=df, ax=ax)

ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
ax.set_ylabel("Persentase (%)")
ax.set_title("Persentase Realisasi Anggaran terhadap Rencana")
ax.axhline(100, color="red", linestyle="--")

# label persentase 
for p, value in zip(ax.patches, df["Realisasi_vs_Rencana_Anggaran"]):
    ax.text(
        p.get_x() + p.get_width() / 2,
        p.get_height() + 1,
        f"{value:.1f}%",
        ha="center",
        va="bottom",
        fontsize=8,
        rotation=0,
        fontweight="bold"
    )

st.pyplot(fig)

#   3. HUBUNGAN DATA

# Heatmap korelasi
st.subheader("3. Heatmap Korelasi")

corr = df[[
    "Realisasi_Jumlah_KPM",
    "Realisasi_Anggaran",
    "Rencana_Jumlah_KPM",
    "Rencana_Anggaran"
]].corr()

fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, ax=ax)
st.pyplot(fig)


#   4. CLUSTERING 

st.subheader("4. Clustering Provinsi Berdasarkan Kebutuhan Bantuan Sosial")

#  skala anggaran ke per 10 juta
df["Realisasi_Anggaran_10Juta"] = df["Realisasi_Anggaran"] / 10_000_000

# jitter 
import numpy as np
df["KPM_jitter"] = df["Realisasi_Jumlah_KPM"] + np.random.uniform(-0.5, 0.5, size=len(df))
df["Anggaran_jitter"] = df["Realisasi_Anggaran_10Juta"] + np.random.uniform(-0.3, 0.3, size=len(df))

fig, ax = plt.subplots(figsize=(12, 7))

sns.scatterplot(
    x="KPM_jitter",
    y="Anggaran_jitter",
    hue="Cluster",
    palette="tab10",
    data=df,
    s=220,
    alpha=0.7,
    edgecolor="black"
)

ax.set_xlabel("Jumlah KPM (Keluarga Penerima Manfaat)")
ax.set_ylabel("Anggaran (dalam satuan 10 Juta Rupiah)")
ax.set_title("Clustering Provinsi Berdasarkan Kebutuhan Bantuan Sosial")

ax.grid(True, linestyle="--", alpha=0.5)

# label provinsi 
for i in range(df.shape[0]):
    ax.text(
        df["KPM_jitter"].iloc[i] + 0.5,
        df["Anggaran_jitter"].iloc[i] + 0.5,
        df["Provinsi"].iloc[i],
        fontsize=9,
        weight="bold"
    )

st.pyplot(fig)

st.subheader("Rangkuman Per Cluster (Rata-Rata)")
summary = df.groupby("Cluster")[["Realisasi_Jumlah_KPM", "Realisasi_Anggaran"]].mean()
summary["Realisasi_Anggaran (Rp)"] = summary["Realisasi_Anggaran"].apply(lambda x: f"{x:,.0f}")
summary.drop(columns=["Realisasi_Anggaran"], inplace=True)

st.dataframe(summary)
