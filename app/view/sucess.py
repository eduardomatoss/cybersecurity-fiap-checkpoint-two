import streamlit as st


def sucess_page():
    st.header("Pix successfully performed!!")

    st.balloons()

    gifList = [
        "https://media.giphy.com/media/X8WNVwXFnYWUMFnI4z/giphy.gif",
        "https://media.giphy.com/media/zFdHAFsieZ7LawRKyW/giphy.gif"
    ]

    for i in gifList:
        st.markdown(f"![Alt Text]({i})")
