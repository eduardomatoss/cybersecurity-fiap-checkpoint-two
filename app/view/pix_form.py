import streamlit as st

from app.services.form_checker import form_main_checker
from app.services.media_recorder import record_audio
from app.services.media_recorder import save_record
from app.services.speech_recognizer import to_text
from app.common.enumerators import SECRET_WORD


def pix_transfer():
    st.title("Pix Transfer")
    st.text("Step 2/2")

    pix_value = st.number_input("Pix value")

    if pix_value > 0.1:
        st.warning("Your security key")
        if st.button("Record"):
            with st.spinner("Recording for 3 seconds ...."):
                if record_media():
                    st.success("Authorized transaction")
                else:
                    st.error("Unauthorized transaction")

        if st.button("Submit"):
            form_main_checker(st.session_state.form)
            st.experimental_rerun()


def record_media() -> bool:
    file_path = "./record/recorded_pix_audio.wav"
    record = record_audio()
    save_record(file_path, record)
    if to_text(file_path) == SECRET_WORD:
        return True
    return False
