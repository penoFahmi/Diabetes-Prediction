import streamlit as st
from home import show as show_home
from prediction import show as show_prediction
from about import show as show_about
from footer import show as show_footer

# Sidebar untuk navigasi
st.sidebar.title("📚 Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Beranda", "Prediksi", "Tentang"])

# Logika untuk menampilkan halaman sesuai pilihan
if menu == "Beranda":
    show_home()
elif menu == "Prediksi":
    show_prediction()
elif menu == "Tentang":
    show_about()

# Menambahkan footer di bawah halaman dengan HTML dan CSS
show_footer()
