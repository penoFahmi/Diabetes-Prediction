import streamlit as st

def show():
    # Set konfigurasi halaman
    st.set_page_config(
        page_title="Prediksi Risiko Diabetes",
        layout="wide",
        initial_sidebar_state="expanded"
    )

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

    st.image("../img/output.png", caption="Gambaran Visual Analisis Data", use_column_width=True)

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
        st.image("../img/matrik.png", caption="Hubungan Antara Variabel")
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
        st.image("../img/output.png", caption="Distribusi Parameter Kesehatan")

    st.write("---")

    # Hasil prediksi
    st.subheader("🤖 **Hasil Prediksi dengan XGBoost**")
    st.image("img/xgboost.png", caption="Hasil Prediksi: Hubungan Antara Nilai Aktual dan Prediksi")
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

# Menjalankan aplikasi
if __name__ == "__main__":
    show()
