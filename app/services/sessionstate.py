import streamlit as st


def sessionstate_declare():
    if "step" not in st.session_state:
        st.session_state.step = 0

    if "form" not in st.session_state:
        st.session_state.form = {}
