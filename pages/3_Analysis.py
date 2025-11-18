import streamlit as st
from sklearn.cluster import KMeans

st.title("📊 Analysis")

if "clean_data" not in st.session_state:
    st.warning("Lakukan preprocessing terlebih dahulu!")
else:
    data = st.session_state["clean_data"]

    st.write("Pilih kolom yang akan digunakan untuk clustering:")
    selected = st.multiselect("Kolom numerik:", data.select_dtypes(include="number").columns)

    if len(selected) > 0:
        k = st.slider("Jumlah Cluster", 2, 6, 3)

        kmeans = KMeans(n_clusters=k)
        data["Cluster"] = kmeans.fit_predict(data[selected])

        st.write(data.head())
        st.success("Clustering berhasil dilakukan!")

        st.session_state["cluster_data"] = data
