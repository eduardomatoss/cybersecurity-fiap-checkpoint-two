import streamlit as st


def sucess_page():
    st.header("Verificado com sucesso!!")

    st.balloons()

    gifList = [
        "https://media.giphy.com/media/gQ2TrLmmvN19eV0mqB/giphy.gif",
        "https://media.giphy.com/media/9DgxhWOxHDHtF8bvwl/giphy.gif",
        "https://media.giphy.com/media/3o6ZtiwjWMoRIpJiIE/giphy.gif",
    ]

    for i in gifList:
        st.markdown(f"![Alt Text]({i})")
