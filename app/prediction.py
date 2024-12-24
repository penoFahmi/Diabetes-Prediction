# import streamlit as st
# import numpy as np
# import os
# import pickle

# # Tentukan direktori untuk file model
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(BASE_DIR, "../models/best_xgb_model.pkl")

# # Memuat model menggunakan pickle
# with open(model_path, "rb") as file:
#     model = pickle.load(file)

# # Verifikasi model berhasil dimuat
# print("Model berhasil dimuat")

# # # Judul aplikasi
# # st.title("Aplikasi Prediksi Risiko Diabetes")
# # st.write("Masukkan data pasien untuk memprediksi kemungkinan diabetes.")

# # # Input fitur yang sesuai dengan model
# # medication_adherence = st.number_input("Kepatuhan Minum Obat (%)", min_value=0.0, max_value=100.0, value=80.0)
# # bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=0.0, max_value=100.0, value=25.0)
# # diet = st.number_input("Skor Pola Makan (0-100)", min_value=0.0, max_value=100.0, value=70.0)
# # stress_level = st.number_input("Tingkat Stres (0-100)", min_value=0.0, max_value=100.0, value=50.0)
# # physical_activity = st.number_input("Aktivitas Fisik (Jam/Minggu)", min_value=0.0, max_value=100.0, value=5.0)
# # hydration_level = st.number_input("Tingkat Hidrasi (Liter/Hari)", min_value=0.0, max_value=10.0, value=2.0)
# # blood_glucose = st.number_input("Kadar Glukosa Darah (mg/dL)", min_value=0.0, max_value=300.0, value=110.0)
# # sleep_hours = st.number_input("Durasi Tidur (Jam/Hari)", min_value=0.0, max_value=24.0, value=7.0)
# # weight = st.number_input("Berat Badan (kg)", min_value=0.0, max_value=300.0, value=70.0)
# # heigt = st.number_input("Tinggi Badan (m)", min_value=0.0, max_value=250.0, value=170.0)

# # # Membuat array input untuk prediksi (sesuai dengan jumlah fitur model, yaitu 9)
# # input_data = np.array([[medication_adherence, bmi, diet, stress_level, physical_activity,
# #                         hydration_level, blood_glucose, sleep_hours, weight]])


# # Judul aplikasi
# st.title("Prediksi Risk Score Diabetes")

# # Penjelasan singkat
# st.write("""
# Aplikasi ini memprediksi **risk score diabetes** berdasarkan parameter kesehatan.
# Masukkan data Anda untuk mendapatkan hasil prediksi.
# """)

# st.markdown("""
# ### Apa itu Diabetes?
# Diabetes adalah kondisi kronis yang memengaruhi kemampuan tubuh untuk memproses glukosa darah. Beberapa faktor risiko meliputi:
# - **Gaya hidup sedentary:** Kurangnya aktivitas fisik.
# - **Pola makan yang buruk:** Tinggi gula, lemak jenuh, dan rendah serat.
# - **Riwayat keluarga:** Faktor genetik berperan penting.
# - **Stres kronis:** Dapat memengaruhi kadar gula darah.
# - **Kurang tidur:** Berkontribusi pada resistensi insulin.

# #### Pencegahan:
# - **Pola makan sehat:** Perbanyak buah, sayur, dan makanan berserat.
# - **Aktivitas fisik:** Lakukan olahraga setidaknya 30 menit setiap hari.
# - **Manajemen stres:** Hindari tekanan berlebihan dengan relaksasi.
# - **Cukup tidur:** Pastikan 7-9 jam tidur berkualitas setiap malam.
# """)


# # Penjelasan singkat tentang aplikasi
# st.write("""
# Aplikasi ini membantu Anda memprediksi **persentase risiko diabetes** berdasarkan data kesehatan yang dimasukkan. 
# Ikuti langkah-langkah di bawah ini untuk menggunakan aplikasi:
# 1. Isi data kesehatan Anda seperti berat badan, tinggi badan, kadar glukosa, dan lainnya.
# 2. Klik tombol **Prediksi** untuk melihat hasil.
# 3. Hasil akan menampilkan persentase risiko diabetes berdasarkan data yang dimasukkan.
# """)

# # Input pengguna
# st.subheader("Silakan masukkan data kesehatan Anda:")
# weight = st.number_input("Berat badan (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)
# height = st.number_input("Tinggi badan (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
# blood_glucose = st.number_input("Kadar glukosa darah", min_value=50.0, max_value=300.0, value=120.0, step=0.1)
# physical_activity = st.slider("Aktivitas fisik (jam/hari)", min_value=0.0, max_value=24.0, value=1.0, step=0.1)
# diet = st.selectbox("Kepatuhan diet (1 = ya, 0 = tidak)", [1, 0])
# medication_adherence = st.selectbox("Kepatuhan konsumsi obat (1 = ya, 0 = tidak)", [1, 0])
# stress_level = st.slider("Tingkat stres (1 = rendah, 2 = sedang, 3 = tinggi)", min_value=1, max_value=3, value=2)
# sleep_hours = st.number_input("Jam tidur (jam/hari)", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
# hydration_level = st.selectbox("Hidrasi (1 = cukup, 0 = kurang)", [1, 0])
# bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)

# # Tombol prediksi
# if st.button("Prediksi"):
#     # Membuat array input untuk prediksi (sesuai dengan jumlah fitur model, yaitu 9)
#     input_data = np.array([[medication_adherence, bmi, diet, stress_level, physical_activity,
#                         hydration_level, blood_glucose, sleep_hours, weight]])

    
#     # Prediksi menggunakan model
#     prediction = model.predict(input_data)[0]
    
#     # Hasil prediksi
#     st.success(f"Risk Score Prediksi: {prediction:.2f} %")


# # Survei feedback
# st.markdown("""
# ### Berikan Feedback Anda
# Kami ingin mendengar pendapat Anda mengenai aplikasi ini! Silakan isi survei berikut untuk membantu kami meningkatkan layanan:
# [**Isi Survei**](https://forms.gle/81rTBpgtWzzoFfYS7)
# """)

# # Footer
# st.markdown("""
# ---
# © 2024 Aplikasi Prediksi Risiko Diabetes | Dibuat dengan ❤️ menggunakan [Streamlit](https://streamlit.io/)
# """)



# REVISI YANG SEMANGAT
import streamlit as st
import numpy as np
import os
import pickle

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/best_xgb_model.pkl")

# Memuat model
with open(model_path, "rb") as file:
    model = pickle.load(file)

def show():
    st.title("🔍 Prediksi Risiko Diabetes")
    st.subheader("📝 Masukkan Data Kesehatan Anda:")

    # Input pengguna
    weight = st.number_input("Berat badan (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.1)
    height = st.number_input("Tinggi badan (cm)", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    blood_glucose = st.number_input("Kadar glukosa darah (mg/dL)", min_value=50.0, max_value=300.0, value=120.0, step=0.1)
    physical_activity = st.slider("Aktivitas fisik (jam/hari)", min_value=0.0, max_value=24.0, value=1.0, step=0.1)
    diet = st.selectbox("Kepatuhan diet (1 = Ya, 0 = Tidak)", [1, 0])
    medication_adherence = st.selectbox("Kepatuhan konsumsi obat (1 = Ya, 0 = Tidak)", [1, 0])
    stress_level = st.slider("Tingkat stres (1 = Rendah, 2 = Sedang, 3 = Tinggi)", min_value=1, max_value=3, value=2)
    sleep_hours = st.number_input("Jam tidur (jam/hari)", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
    hydration_level = st.selectbox("Hidrasi (1 = Cukup, 0 = Kurang)", [1, 0])

    # Tombol prediksi
    if st.button("Prediksi"):
        input_data = np.array([[medication_adherence, bmi, diet, stress_level, physical_activity,
                                hydration_level, blood_glucose, sleep_hours, weight]])
        prediction = model.predict(input_data)[0]
        st.success(f"✨ Risk Score Prediksi: {prediction:.2f} %")
        st.write("""
        **Catatan:** Hasil prediksi adalah estimasi. Konsultasikan dengan profesional medis untuk informasi lebih lanjut.
        """)
