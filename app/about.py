import streamlit as st

def show():
    st.title("ℹ️ Tentang Aplikasi")
    st.write("""
    Aplikasi ini dirancang untuk membantu pengguna memprediksi risiko diabetes berdasarkan data kesehatan mereka.
    
    **Tujuan Aplikasi**:
    - Memberikan prediksi risiko diabetes dengan cepat dan mudah.
    - Meningkatkan kesadaran pengguna tentang pentingnya kesehatan.

    **Teknologi yang digunakan**:
    - Python
    - Streamlit
    - Machine Learning
    """)
    st.image("https://via.placeholder.com/800x400?text=Tim+Pengembang", use_column_width=True)
    st.write("""
    **Dikembangkan oleh:**
    - Nama: Peno
    - Posisi: Mahasiswa
    - Email: penofahmi@gmail.com
    """)
