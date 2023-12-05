# Natural-Language-Processing---Transcription-and-summarization
In this repository lies the corresponding Python code for the implementation of two Natural Language Processing technologies for both tasks of transcription and summarization.

# About the project
The project was developed using Streamlit, a web development framework for data science and artificial intelligence projects. Simultaneously, two NLP tools were implemented through their API. The first one was Whisper, which, being a specialized model in voice transcription to convert acoustic signals into text, performed accurate transcription of audio files. The second one was OpenAI's GPT-3.5-turbo, which, being a state-of-the-art language model, was able to comprehend and generate contextual and concise text, providing coherent and relevant responses based on the transcription done by Whisper. It's worth mentioning that it was necessary to use the OpenAI API key to access the GPT-3.5-turbo model.

The process requires the user to provide an m4a audio file so that Whisper and GPT-3.5-turbo can perform their transcription and summarization functions, respectively. If the file is uploaded successfully, a success notification will be displayed. Subsequently, the user should press the "Transcribe and Summarize" button to trigger the instruction for Whisper and GPT-3.5-turbo to perform their tasks on the attached file. Once the information has been processed, the result will be displayed below the "Transcribe and Summarize" button.

## About the Streamlit interface
La interfaz de Streamlit ofrece dos secciones: **Inicio** y **Transcripción y resumen**. En la primera se desglosa un resumen del objetivo y finalidad del proyecto, además de mostrar información de la autoría de este trabajo. En la segunda sección se lleva a cabo el proceso de transcripción y resumen como ya se mencionó anteriormente.
# How to use the python code?
It is recommended to use the code on a Conda Environment (Anaconda) due to its easy installation of dependencies and libraries. It was originally run on a Conda Environment.

# Python libraries
In order to install the corresponding libraries used in the python code just acces to your Conda Environment trough the Anaconda Prompt by following the command:
- conda activate {name of the environment}

Then install the corresponding libraries:
- conda install -c conda-forge ffmpeg
pip install openai
pip install whisper
pip install streamlit

