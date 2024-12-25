import streamlit as st
from home import show as show_home
from prediction import show as show_prediction
from about import show as show_about
from footer import show as show_footer
from streamlit_option_menu import option_menu

def sidebar():
    with st.sidebar:
        # Gaya Sidebar
        st.markdown("""
        <style>
        .css-1aumxhk { 
            background-color: #2e4053 !important;
        }
        .css-qrbaxs { 
            font-size: 18px !important; 
            color: white !important; 
        }
        .css-qrbaxs:hover {
            color: #f39c12 !important;
        }
        </style>
        """, unsafe_allow_html=True)

        # Menu Navigasi dengan Ikon
        selected = option_menu(
            menu_title="📚 Navigasi",  # Judul Sidebar
            options=["Beranda", "Prediksi", "Tentang"],  # Pilihan Menu
            icons=["house", "activity", "info-circle"],  # Ikon dari FontAwesome
            menu_icon="list",  # Ikon untuk menu
            default_index=0,  # Pilihan default
            styles={
                "container": {"padding": "5px", "background-color": "#2e4053"},
                "icon": {"color": "orange", "font-size": "18px"},
                "nav-link": {"font-size": "16px", "color": "white", "text-align": "left", "margin": "0px"},
                "nav-link-selected": {"background-color": "#f39c12"},
            }
        )
        return selected

# Sidebar Navigasi
menu = sidebar()

# Inisialisasi session_state untuk navigasi jika belum ada
if "page" not in st.session_state:
    st.session_state["page"] = "home"

# Update session_state berdasarkan pilihan menu
if menu == "Beranda":
    st.session_state["page"] = "home"
elif menu == "Prediksi":
    st.session_state["page"] = "prediction"
elif menu == "Tentang":
    st.session_state["page"] = "about"

# Logika untuk menampilkan halaman sesuai dengan nilai session_state["page"]
if st.session_state["page"] == "home":
    show_home()
elif st.session_state["page"] == "prediction":
    show_prediction()
elif st.session_state["page"] == "about":
    show_about()

# Footer
show_footer()
