import streamlit as st


def front():

    text = """
           Hola! por acá TAETT. Basandonos en codigo de SPAIN AI implementaremos "**Extractive Question Answering**" sobre contenido de obras de arquitectura. Los modelos NLP serán provistos por Huggingface. Los textos de Plataforma Arquitectura
            
            """
    st.write(text)

    image_huggingface_url = "http://rarasartes.com/wp-content/uploads/2018/12/MASP-1.jpg"
    st.image(image_huggingface_url)

    text = "MASP en PlataformaArquitectura"
    url = "https://www.plataformaarquitectura.cl/cl/02-98467/clasicos-de-arquitectura-museo-de-arte-de-sao-paulo-lina-bo-bardi"
    link = "[%s](%s)" % (text, url)
    st.write(link)
