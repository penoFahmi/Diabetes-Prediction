import streamlit as st
from app import home, prediction, about

# Sidebar untuk navigasi
st.sidebar.title("📚 Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Beranda", "Prediksi", "Tentang"])

# Logika untuk menampilkan halaman sesuai pilihan
if menu == "Beranda":
    home.show()
elif menu == "Prediksi":
    prediction.show()
elif menu == "Tentang":
    about.show()

# Menambahkan footer di bawah halaman dengan HTML dan CSS
st.markdown("""
    <style>
    footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #2e4053;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
    }
    </style>
    <footer>
        © 2024 Prediksi Risiko Diabetes | Create by PENO & ARIEL
    </footer>
""", unsafe_allow_html=True)
