import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

import streamlit as st

st.set_page_config(
    page_title="Analisis Bansos Pangan Indonesia",
    layout="wide"
)

st.title("📊 Dashboard Analisis Bantuan Sosial Pangan Indonesia")

st.write("""
Selamat datang di dashboard analisis bantuan sosial pangan.  
Gunakan menu di sidebar untuk mengakses:
- Input Data
- Preprocessing
- Analysis
- Visualization
- About Us
""")
