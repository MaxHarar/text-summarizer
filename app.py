import streamlit as st
import openai
import os
from text_summarizer.functions import summarize

from dotenv import load_dotenv
load_dotenv()


openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_base = os.getenv("ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
openai.api_key = os.getenv("OPENAI_API_KEY")


if "summary" not in st.session_state:
    st.session_state["summary"] = ""
if "compared_summary" not in st.session_state:
    st.session_state["compared_summary"] = ""

st.title("Text Summarizer")

# Dropdown for knowledge level options
knowledge_level_options = ["beginner", "intermediate", "advanced", "expert", "specialist"]
selected_knowledge_level = st.selectbox("Select your knowledge level:", knowledge_level_options)

input_text = st.text_area(label="Enter full text:", value="", height=250)


##change
# "Submit" button  generate summary at the selected knowledge level
if st.button(
    "Submit",
    on_click=summarize,
    kwargs={"prompt": input_text, "knowledge_level": selected_knowledge_level},
):
    st.session_state["summary"] = st.session_state["summary"]

output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
