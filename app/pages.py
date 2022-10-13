import streamlit as st

from app.view.registration_form import registration
from app.view.pix_form import pix_transfer
from app.view.page_title import page_title
from app.services.sessionstate import sessionstate_declare
from app.view.sucess import sucess_page


def startup():
    sessionstate_declare()
    page_title()

    match st.session_state.step:

        case 0:
            registration()

        case 1:
            pix_transfer()

        case 2:
            sucess_page()
