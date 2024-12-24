import streamlit as st

def show():
    st.markdown("""
    <style>
    footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #2e4053;
        color: white;
        text-align: center;
        padding: 10px 0;
        font-size: 14px;
    }
    </style>
    <footer>
        © 2024 Prediksi Risiko Diabetes | CREATE by Peno & Ariel
    </footer>
    """, unsafe_allow_html=True)
