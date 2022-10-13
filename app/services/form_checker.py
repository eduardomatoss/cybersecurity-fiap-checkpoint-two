import streamlit as st

from time import sleep


def form_main_checker(form: dict):

    match st.session_state.step:

        case 0:
            if form["name"] == "":
                st.error("Name is empty")
                sleep(2)

            elif form["lname"] == "":
                st.error("Last Name is empty")
                sleep(2)

            else:
                st.session_state.step = 1

        case 1:

            st.session_state.step = 2

        case 2:

            st.session_state.step = 3
