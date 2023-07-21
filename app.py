## streamlit run app.py

import streamlit as st
import openai
import os
from text_summarizer.functions import summarize

# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_KEY')

if "summary" not in st.session_state:
    st.session_state["summary"] = ""

st.title("Text Summarizer")

# Dropdown for knowledge level options
knowledge_level_options = ["beginner", "intermediate", "advanced", "expert", "specialist"]
selected_knowledge_level = st.selectbox("Select your knowledge level:", knowledge_level_options)

input_text = st.text_area(label="Enter full text:", value="", height=250)

st.button(
    "Submit",
    on_click=summarize,
    kwargs={"prompt": input_text, "knowledge_level": selected_knowledge_level},  # Pass the selected knowledge level
)

output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)



""""""