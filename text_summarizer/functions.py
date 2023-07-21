import openai
import streamlit as st

def summarize(prompt, knowledge_level):
    if knowledge_level == "beginner":
        augmented_prompt = f"Explain this medical information, concisely in simple terms for someone new to medicine, if there are medicial words that you deem complex, please make sure to explain what they are: {prompt}"
    elif knowledge_level == "intermediate":
        augmented_prompt = f"Summarize this medical information for someone with some medical knowledge: {prompt}"
    elif knowledge_level == "advanced":
        augmented_prompt = f"Provide a detailed summary of this medical information for someone with advanced medical knowledge: {prompt}"
    elif knowledge_level == "expert":
        augmented_prompt = f"Give an expert-level analysis of this medical information: {prompt}"
    elif knowledge_level == "specialist":
        augmented_prompt = f"Delve into the specifics of this medical information as if explaining it to a specialist: {prompt}"
    else:
        augmented_prompt = prompt

    st.session_state["summary"] = openai.Completion.create(
        model="text-davinci-003",
        prompt=augmented_prompt,
        temperature=.5,
        max_tokens=1000,
    )["choices"][0]["text"]
