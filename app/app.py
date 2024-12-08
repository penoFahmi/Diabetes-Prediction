import streamlit as st
import joblib
import numpy as np
import os
import pickle


# Memuat model dari file .pkl
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "../models/best_xgb_model.pkl")
# model = joblib.load(model_path)
# model_path = "../models/best_xgb_model.pkl"  # Pastikan jalur ini sesuai
with open(model_path, "rb") as file:
    model = pickle.load(file)



# Judul aplikasi
st.title("Aplikasi Prediksi Diabetes")
st.write("Masukkan data pasien untuk memprediksi kemungkinan diabetes.")

# Input fitur yang sesuai dengan model
pregnancies = st.number_input("Jumlah Kehamilan", min_value=0, max_value=20, value=1)
glucose = st.number_input("Kadar Glukosa", min_value=0.0, max_value=300.0, value=120.0)
blood_pressure = st.number_input("Tekanan Darah", min_value=0.0, max_value=200.0, value=80.0)
skin_thickness = st.number_input("Ketebalan Kulit", min_value=0.0, max_value=100.0, value=20.0)
insulin = st.number_input("Kadar Insulin", min_value=0.0, max_value=1000.0, value=85.0)
bmi = st.number_input("Indeks Massa Tubuh (BMI)", min_value=0.0, max_value=100.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.0, value=0.5)
age = st.number_input("Usia", min_value=0, max_value=120, value=30)

# Tambahan fitur ke-9: kategori BMI (contoh)
kategori_bmi = st.selectbox(
    "Kategori BMI",
    options=["Underweight", "Normal", "Overweight", "Obesity"]
)

# Encode kategori BMI menjadi angka
kategori_bmi_encoded = {"Underweight": 0, "Normal": 1, "Overweight": 2, "Obesity": 3}[kategori_bmi]

# Membuat array input untuk prediksi
input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age, kategori_bmi_encoded]])

# Tombol untuk memulai prediksi
if st.button("Prediksi"):
    try:
        prediction = model.predict(input_data)
        result = "Diabetes Terdeteksi" if prediction[0] == 1 else "Tidak Ada Diabetes"
        st.write(f"Hasil Prediksi: {result}")
    except ValueError as e:
        st.error(f"Terjadi kesalahan: {e}")
