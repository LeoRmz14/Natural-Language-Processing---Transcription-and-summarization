# Para que funcione el código es necesario correrlo en un ambiente de anaconda (Conda environment). El environment utilizado fue el llamado "prueba" pues se le instalaron
# las respectivas dependencias y librerías requeridas como ffmpeg, opneai, streamlit, etc.

import streamlit as st
import openai
import whisper
import numpy as np
import os 

# Configuración de OpenAI
openai.api_key = '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'
model = whisper.load_model("base")
file_path = 'MA1.m4a'

# Inicialización de las funciones de transcripción y resumen

@st.cache(suppress_st_warning=True, show_spinner=False) # Se utiliza cache para que streamlit no se reinicie cuando se le carga el archivo con st.file_uploader
def transcribe_audio(model,file_path):
    try:
        transcript = model.transcribe(file_path)
        return transcript["text"]
    except Exception as e:
        st.error(f"Error durante la transcripción: {e}")
        return ""

def custom_chatgpt(user_input):
    messages = [
        {"role": "system", "content": "You are an office administrator, summarize the text in key points"},
        {"role": "user", "content": user_input},
    ]
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chatgpt_reply = response["choices"][0]["message"]["content"]
        return chatgpt_reply
    except Exception as e:
        st.error(f"Error in ChatGPT response: {e}")
        return ""

# Función principal de la aplicación Streamlit
def main():
    st.title("Página en Streamlit")

    # Botones en la barra lateral
    opcion_seleccionada = st.sidebar.radio("Seleccione una opción:", ["Inicio/Portada", "Transcripción de audio y resumen"])

    if opcion_seleccionada == "Inicio/Portada":
        mostrar_inicio()
    elif opcion_seleccionada == "Transcripción de audio y resumen":
        mostrar_nlp()

def mostrar_inicio():
    st.title("Bienvenido a mi página de Inicio")
    st.markdown("---")
    st.header("Leonardo Ramírez Ramírez - A01351715 ")
    st.subheader("Equipo 1")
    st.markdown(
        """
        <div style="text-align: center;">
            La presente página web fue desarrollada para la clase <b>Procesamiento de Lenguaje Natural</b> como parte de la segunda parte de la concentración en 
            <b>Inteligencia Artificial Avanzada para la Ciencia de Datos</b>
        </div>
        """,
        unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("Objetivo de la página")
    st.markdown(
        """
        <div style="text-align: center;">
            El objetivo de la página es poner en práctica las competencias aprendidas en las clases de <b>Procesamiento de Lenguaje Natural</b>, siendo éstas:
        </div>
        """,
        unsafe_allow_html=True)
    st.markdown("""
    - Desarrollar una interfaz que llame a APIs de Lenguaje Natural.
    - Desarrollar una interfaz que llame a APIs de Reconocimiento de Voz.
    - Utilizar APIs de Procesamiento Natural de Lenguaje: Análisis de Sentimientos, Clasificación, Traducción, etc.
    """)
    st.write("Vaya al botón Transcripción de audio y resúmen para comenzar con la experiencia de NLP")
    

def mostrar_nlp():
    st.header("Bienvenido, ¡comencemos!")
    st.markdown("---")
    st.subheader("¿Cómo funciona?")
    st.write("Arrastre/Seleccione su archivo con extensión .m4a para que el audio sea procesado y resumido. La transcripción se realizó con la biblioteca Whisper y el resumen de texto se realizó con la API de ChatGPT")               
    st.markdown("""
    - **Cargue el archivo**: Cargue el archivo .m4a.
    - **Transcribir y resumir**: Presione el botón Transcribir y resumir. 
    - **Transcripción de video y resumen**: Obtenga la transcripción del video en formato string así como su resumen en forma de bullets.
    """)
    st.markdown("---")
    st.subheader("Cargue el archivo:")
    uploaded_file = st.file_uploader("Choose a file", type=["m4a"])
    file_path = 'MA1.m4a'
    if uploaded_file is not None:
        nombre_archivo = uploaded_file.name
        st.success(f"Archivo '{nombre_archivo}' cargado correctamente!")

    if st.button("Transcribir y resumir"):
        # Mostrar spinner mientras se realizan las tareas
        with st.spinner("Realizando transcripción y resumen... Esto puede llevar tiempo."):
            # Transcribir el archivo
            st.text("Realizando transcripción... Esto puede llevar tiempo.")
            transcription = transcribe_audio(model, file_path)

            # Resumir la transcripción
            st.text("Realizando resumen... Esto puede llevar tiempo.")
            summary = custom_chatgpt(transcription)

        # Mostrar resultados
        st.subheader("Transcripción:")
        st.write(transcription)

        st.subheader("Resumen:")
        st.write(summary)





if __name__ == "__main__":
    main()
