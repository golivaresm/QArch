import streamlit as st


def sidebar(ls_page_name):

    # Resources
    image_spainai_url = "https://taett.cl/wp-content/uploads/2021/11/TAETT.png"
    edition = "TAETT"
    title = "# Vamos a explorar"

    st.sidebar.image(image_spainai_url)
    st.sidebar.write(edition)
    st.sidebar.write(title)
    page_name = st.sidebar.selectbox("", ls_page_name)

    return page_name
