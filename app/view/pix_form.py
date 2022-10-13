import streamlit as st

from app.services.form_checker import form_main_checker


def pix_transfer():
    st.title("Pix Transfer")
    st.text("Step 2/2")

    pix_value = st.number_input("Pix value")

    if pix_value > 0.1:
        st.warning("Your security key")
        if st.button("Record"):
            with st.spinner("Recording for 10 seconds ...."):
                # record()
                st.success("Recording completed")

        if st.button("Submit"):
            form_main_checker(st.session_state.form)
            st.experimental_rerun()
