import openai
import streamlit as st


def summarize(prompt, knowledge_level):
    if knowledge_level == "beginner":
        augmented_prompt = f"Explain this medical information, concisely in simple terms for someone new to medicine, if there are medical words that you deem complex, please make sure to explain what they are: {prompt}"
    elif knowledge_level == "intermediate":
        augmented_prompt = f"Summarize this medical information for someone with some medical knowledge: {prompt}"
    elif knowledge_level == "advanced":
        augmented_prompt = f"Provide a detailed summary of this medical information for someone with advanced medical knowledge: {prompt}"
    elif knowledge_level == "expert":
        augmented_prompt = f"Give an expert-level summary of this medical information: {prompt}"
    elif knowledge_level == "specialist":
        augmented_prompt = f"Delve into the specifics of this medical information as if explaining it to a specialist: {prompt}"
    else:
        augmented_prompt = prompt

    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo",
        messages=[
            {"role": "system",
             "content": f"You are a helpful medical specialist explaining and summarizing the information to someone of a  '{knowledge_level}' knowledge level regarding medicine."},
            {"role": "user", "content": augmented_prompt}
        ]
    )
    # print(response)

    st.session_state["summary"] = response['choices'][0]['message']['content']

