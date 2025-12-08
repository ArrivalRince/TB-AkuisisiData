import streamlit as st

# header
st.markdown("""
    <div style="
        background: linear-gradient(90deg, #4992b7, #2575FC);
        padding: 15px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 10px;">
        <h2 style="text-align:center; margin-top: -20px;">
             Tugas Besar Akuisisi Data
        </h2>
        <p style="font-size:16px; margin:0;">
           Analisis Bantuan Sosial Pangan Indonesia
        </p>
    </div>
""", unsafe_allow_html=True)

#card style
card_style = """
<style>
.card {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    border-left: 6px solid #4992b7;
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 6px 20px rgba(0,0,0,0.15);
}
.card-title {
    font-size: 19px;
    font-weight: bold;
    color: #003F86;
}
.card-desc {
    font-size: 14px;
    color: #444444;
    margin-top: 9px;
    text-align: left;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

#sejajarkan card
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title"> Gambaran Umum Tugas Besar</div>
        <div class="card-desc">
        Tugas besar ini menganalisis pemerataan dan efektivitas 
        <b>Bantuan Sosial Pangan</b> di seluruh provinsi Indonesia.  
        Dataset mencakup rencana serta realisasi <b>jumlah KPM</b> dan <b>anggaran</b>.  
        Analisis dilakukan melalui preprocessing, visualisasi data, dan <b>clustering K-Means</b>.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">Tujuan Utama Dashboard Ini</div>
        <ul>
            <li>Hubungan realisasi KPM dan anggaran</li>
            <li>Pemetaan cluster provinsi berdasarkan tingkat bansos</li>
            <li>Identifikasi provinsi dengan realisasi tertinggi & terendah</li>
        </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <div class="card-title">Alur Penggunaan</div>
        <ol>
            <li><b>Input Data</b> – unggah dataset bansos.</li>
            <li><b>Preprocessing</b> – bersihkan dan siapkan data.</li>
            <li><b>Analysis</b> – lakukan analisis & clustering.</li>
            <li><b>Visualization</b> – lihat grafik dan interpretasi hasil.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.write("---")
