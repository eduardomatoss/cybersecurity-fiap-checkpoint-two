import streamlit as st


def page_title():
    st.title("Bank XPTO")
    if st.session_state.step != 0:

        if st.button("Back"):
            st.session_state.step -= 1
            st.experimental_rerun()
