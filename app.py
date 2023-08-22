import streamlit as st
import openai
import os
from text_summarizer.functions import summarize

# Set your OpenAI API key
openai.api_key = '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'
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
