import streamlit as st

def show():
    # Header
    st.title("🏥 Tentang Aplikasi Diabetes Risk Predictor")
    st.markdown("""
    Selamat datang di aplikasi **Diabetes Risk Predictor**! Aplikasi ini membantu pengguna memprediksi risiko diabetes berdasarkan data kesehatan mereka.
    """)
    
    # Tujuan
    st.subheader("🎯 Tujuan Aplikasi")
    st.markdown("""
    - **Prediksi Cepat dan Akurat**: Memberikan prediksi risiko diabetes dengan mudah.
    - **Peningkatan Kesadaran**: Membantu pengguna memahami pentingnya kesehatan.
    """)
    
    # Teknologi
    st.subheader("💻 Teknologi yang Digunakan")
    technologies = ["Python", "Streamlit", "Machine Learning"]
    st.markdown("Berikut adalah teknologi utama yang digunakan:")
    for tech in technologies:
        st.markdown(f"- {tech}")

    # # Gambar
    # st.image(
    #     "https://via.placeholder.com/800x400?text=Tim+Pengembang", 
    #     caption="Tim Pengembang",
    #     use_column_width=True
    # )
    
    # Profil Pengembang
    st.subheader("👥 Tim Pengembang")
    team = [
        {"Nama": "Peno", "Posisi": "Mahasiswa", "Email": "penofahmi@gmail.com"},
        {"Nama": "Ariel", "Posisi": "Mahasiswa", "Email": "ariel@gmail.com"}
    ]
    for member in team:
        st.markdown(f"""
        **Nama**: {member['Nama']}  
        **Posisi**: {member['Posisi']}  
        **Email**: {member['Email']}
        """)

# Call the function to render
# if __name__ == "__main__":
#     show()
