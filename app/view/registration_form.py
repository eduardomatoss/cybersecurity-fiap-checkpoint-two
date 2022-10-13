import streamlit as st

from app.services.form_checker import form_main_checker


def registration():

    st.title("Form Registration")
    st.text("Step 1/2")

    st.session_state.form["name"] = st.text_input("Name")
    st.session_state.form["lname"] = st.text_input("Last Name")

    st.text("Safety phrase")
    if st.button("Record"):
        with st.spinner("Recording for 10 seconds ...."):
            # record()
            st.success("Recording completed")

    if st.button("Submit"):
        form_main_checker(st.session_state.form)
        st.experimental_rerun()
