import streamlit as st

st.set_page_config(page_title="About Us", layout="wide")


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
             Tim Pengembang 
        </h2>
        <p style="font-size:16px; margin:0;">
           Kelompok 6 – Sistem Informasi A, Universitas Andalas
        </p>
    </div>
""", unsafe_allow_html=True)

# tim penggembang
st.markdown("""
<style>
.team-card {
    background-color: #ffffff;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    text-align: center;
    transition: 0.3s;
}
.team-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 16px rgba(0,0,0,0.25);
}
.name {
    font-size: 20px; 
    font-weight: bold; 
    margin-top: 10px;
}
.nim {
    font-size: 15px; 
    color: #666;
}
</style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="team-card">
        <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" width="90">
        <div class="name">Asyifa Rahmina Yudi</div>
        <div class="nim">2311521007</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="team-card">
        <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" width="90">
        <div class="name">Arrival Rince Putri</div>
        <div class="nim">2311523019</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="team-card">
        <img src="https://cdn-icons-png.flaticon.com/512/1946/1946429.png" width="90">
        <div class="name">Nala Dewanti</div>
        <div class="nim">2311523029</div>
    </div>
    """, unsafe_allow_html=True)

