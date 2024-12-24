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

# Footer
st.sidebar.markdown("---")
st.sidebar.write("© 2024 Prediksi Risiko Diabetes | Dibuat dengan ❤️ oleh Tim Developer")
