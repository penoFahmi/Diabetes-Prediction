# import streamlit as st
# import numpy as np
# import os
# import pickle


# # # Tentukan direktori untuk file model
# # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# # model_path = os.path.join(BASE_DIR, "../models/best_xgb_model.pkl")

# # # Memuat model menggunakan joblib
# # model = joblib.load(model_path)

# # # Verifikasi model berhasil dimuat
# # print("Model berhasil dimuat")
# # Tentukan direktori untuk file model
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# model_path = os.path.join(BASE_DIR, "../models/best_xgb_model.pkl")

# # Memuat model menggunakan pickle
# with open(model_path, "rb") as file:
#     model = pickle.load(file)

# # Verifikasi model berhasil dimuat
# print("Model berhasil dimuat")




# # Judul aplikasi
# st.title("Aplikasi Prediksi Diabetes")
# st.write("Masukkan data pasien untuk memprediksi kemungkinan diabetes.")

# # Input fitur yang sesuai dengan model
# pregnancies = st.number_input("Jumlah Kehamilan", min_value=0, max_value=20, value=1)
# glucose = st.number_input("Kadar Glukosa", min_value=0.0, max_value=300.0, value=120.0)
# blood_pressure = st.number_input("Tekanan Darah", min_value=0.0, max_value=200.0, value=80.0)
# skin_thickness = st.number_input("Ketebalan Kulit", min_value=0.0, max_value=100.0, value=20.0)
# insulin = st.number_input("Kadar Insulin", min_value=0.0, max_value=1000.0, value=85.0)
# bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=0.0, max_value=100.0, value=25.0)
# dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.0, value=0.5)
# age = st.number_input("Usia", min_value=0, max_value=120, value=30)

# # Tambahan fitur ke-9: kategori BMI (contoh)
# kategori_bmi = st.selectbox(
#     "Kategori BMI",
#     options=["Underweight", "Normal", "Overweight", "Obesity"]
# )

# # Encode kategori BMI menjadi angka
# kategori_bmi_encoded = {"Underweight": 0, "Normal": 1, "Overweight": 2, "Obesity": 3}[kategori_bmi]

# # Membuat array input untuk prediksi
# input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age, kategori_bmi_encoded]])

# # Tombol untuk memulai prediksi
# if st.button("Prediksi"):
#     try:
#         prediction = model.predict(input_data)
#         result = "Diabetes Terdeteksi" if prediction[0] == 1 else "Tidak Ada Diabetes"
#         st.write(f"Hasil Prediksi: {result}")
#     except ValueError as e:
#         st.error(f"Terjadi kesalahan: {e}")


import streamlit as st
import numpy as np
import os
import pickle

# Tentukan direktori untuk file model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/best_xgb_model.pkl")

# Memuat model menggunakan pickle
with open(model_path, "rb") as file:
    model = pickle.load(file)

# Verifikasi model berhasil dimuat
st.success("Model berhasil dimuat!")

# Judul aplikasi
st.title("Aplikasi Prediksi Diabetes")
st.write("Masukkan data pasien untuk memprediksi kemungkinan diabetes.")

# Input sesuai dengan fitur model
medication_adherence = st.number_input("Kepatuhan Minum Obat (0-100%)", min_value=0.0, max_value=100.0, value=80.0)
bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=0.0, max_value=100.0, value=25.0)
diet = st.number_input("Skor Pola Makan (0-100)", min_value=0.0, max_value=100.0, value=70.0)
stress_level = st.number_input("Tingkat Stres (0-100)", min_value=0.0, max_value=100.0, value=50.0)
physical_activity = st.number_input("Aktivitas Fisik (Jam/Minggu)", min_value=0.0, max_value=100.0, value=5.0)
hydration_level = st.number_input("Tingkat Hidrasi (Liter/Hari)", min_value=0.0, max_value=10.0, value=2.0)
blood_glucose = st.number_input("Kadar Glukosa Darah (mg/dL)", min_value=0.0, max_value=300.0, value=110.0)
sleep_hours = st.number_input("Durasi Tidur (Jam/Hari)", min_value=0.0, max_value=24.0, value=7.0)
weight = st.number_input("Berat Badan (kg)", min_value=0.0, max_value=300.0, value=70.0)
height = st.number_input("Tinggi Badan (cm)", min_value=0.0, max_value=300.0, value=170.0)

# Membuat array input untuk prediksi
input_data = np.array([[medication_adherence, bmi, diet, stress_level, physical_activity,
                        hydration_level, blood_glucose, sleep_hours, weight, height]])

# Tombol untuk memulai prediksi
if st.button("Prediksi"):
    try:
        prediction = model.predict(input_data)
        result = "Diabetes Terdeteksi" if prediction[0] == 1 else "Tidak Ada Diabetes"
        st.success(f"Hasil Prediksi: {result}")
    except ValueError as e:
        st.error(f"Terjadi kesalahan: {e}")
