import streamlit as st
from PIL import Image
import os
from prediction import show as show_prediction

# Fungsi untuk memuat gambar
def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    else:
        st.error(f"Gambar tidak ditemukan: {path}")
        return None

# Memuat gambar
# image = load_image('img/output.png')
# image2 = load_image('img/matrik.png')
# image3 = load_image('img/xgboost.png')
image = load_image(os.path.join(os.getcwd(), 'img/output.png'))
image2 = load_image(os.path.join(os.getcwd(), 'img/matrik.png'))
image3 = load_image(os.path.join(os.getcwd(), 'img/xgboost.png'))


def show():
    # Judul dan pengantar
    st.title("🏠 **Prediksi Risiko Diabetes**")
    st.markdown("""
        ### Selamat Datang!
        Aplikasi ini dirancang untuk membantu Anda memahami **risiko diabetes** berdasarkan data kesehatan. 
        Menggunakan **Machine Learning**, aplikasi ini memberikan:
        - Analisis data kesehatan secara visual.
        - Prediksi risiko berbasis model yang andal.
        - Rekomendasi tindakan pencegahan berdasarkan hasil analisis.
    """)
    
    if image:
        st.image(image, caption="Gambaran Visual Analisis Data", use_container_width=True)

    st.write("---")

    # Tombol navigasi ke halaman Prediksi
    st.markdown("""
        ### Mulai Prediksi
        Klik tombol di bawah ini untuk langsung menuju halaman **Prediksi Risiko Diabetes**.
    """)
    if st.button("🔍 Ke Halaman Prediksi"):
        st.session_state["page"] = "prediction"  # Menavigasi ke halaman prediksi saat tombol diklik

    st.write("---")

    # Latar belakang
    st.subheader("🩺 **Latar Belakang**")
    st.markdown("""
        **Diabetes** adalah salah satu penyakit kronis yang paling banyak memengaruhi masyarakat global. Deteksi dini 
        dan perubahan gaya hidup adalah kunci untuk mencegah atau mengelola penyakit ini. Dengan data kesehatan seperti 
        indeks massa tubuh (BMI), kadar glukosa darah, aktivitas fisik, dan pola tidur, kita dapat memprediksi risiko 
        diabetes dan memberikan rekomendasi pencegahan.
    """)

    # Kolom untuk visualisasi dan insight
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("📈 **Matrik Korelasi Variabel**")
        if image2:
            st.image(image2, caption="Hubungan Antara Variabel", use_container_width=True)
        st.markdown("""
        - **BMI** dan **berat badan** memiliki korelasi tinggi (0.87).
        - **Risiko diabetes** berkorelasi negatif dengan aktivitas fisik dan pola makan.
        - Kadar glukosa darah menunjukkan pengaruh signifikan terhadap skor risiko.
        """)

    with col2:
        st.subheader("📊 **Distribusi Data**")
        st.markdown("""
        Data pada aplikasi ini mencakup berbagai parameter kesehatan, seperti:
        - **Kadar Glukosa Darah (blood_glucose)**
        - **Tingkat Aktivitas Fisik (physical_activity)**
        - **Indeks Massa Tubuh (BMI)**
        """)
        if image:
            st.image(image, caption="Distribusi Parameter Kesehatan", use_container_width=True)

    st.write("---")

    # Hasil prediksi
    st.subheader("🤖 **Hasil Prediksi dengan XGBoost**")
    if image3:
        st.image(image3, caption="Hasil Prediksi: Hubungan Antara Nilai Aktual dan Prediksi", use_container_width=True)
    st.markdown("""
        **Model XGBoost** digunakan untuk memprediksi skor risiko diabetes dengan keakuratan tinggi. 
        Garis merah menunjukkan hubungan linear antara nilai aktual dan prediksi.
    """)

    # Footer
    st.write("---")
    st.info("""
    **Disclaimer**: Aplikasi ini bukan pengganti konsultasi medis profesional. Harap konsultasikan dengan dokter 
    untuk diagnosis atau pengobatan yang lebih akurat.
    """)
