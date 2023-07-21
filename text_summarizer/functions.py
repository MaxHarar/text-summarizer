

import openai
import streamlit as st

def summarize(prompt, knowledge_level):
    if knowledge_level == "beginner":
        augmented_prompt = f"Summarize this text as if you were explaining it to someone with beginner-level knowledge: {prompt}"
    elif knowledge_level == "intermediate":
        augmented_prompt = f"Summarize this text as if you were explaining it to someone with intermediate-level knowledge: {prompt}"
    elif knowledge_level == "advanced":
        augmented_prompt = f"Summarize this text as if you were explaining it to someone with advanced-level knowledge: {prompt}"
    elif knowledge_level == "expert":
        augmented_prompt = f"Summarize this text as if you were explaining it to an expert: {prompt}"
    elif knowledge_level == "specialist":
        augmented_prompt = f"Summarize this text as if you were explaining it to a specialist: {prompt}"
    else:
        augmented_prompt = prompt

    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]

