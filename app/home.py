import streamlit as st

def show():
    st.title("🏠 Halaman Utama")
    st.write("""
    Selamat datang di aplikasi **Prediksi Risiko Diabetes**.
    Gunakan menu di sidebar untuk mengakses berbagai fitur aplikasi.
    """)
    st.image("https://via.placeholder.com/800x400?text=Prediksi+Risiko+Diabetes", use_column_width=True)
    st.write("---")
    st.subheader("🩺 Kenapa Aplikasi Ini Penting?")
    st.write("""
    Diabetes adalah salah satu penyakit kronis utama yang dapat dicegah dengan deteksi dini dan perubahan gaya hidup.
    Dengan aplikasi ini, Anda dapat mengenali risiko Anda dan mengambil langkah pencegahan lebih awal.
    """)
