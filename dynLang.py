import openai
import streamlit as st
from text_summarizer.functions import summarize
import os


from dotenv import load_dotenv
load_dotenv()


openai.api_type = "azure"
openai.api_version = "2023-05-15"
openai.api_base = os.getenv("ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
openai.api_key = os.getenv("OPENAI_API_KEY")

# Knowledge levels for the dropdown menu
knowledge_level_options = ["Beginner", "Intermediate", "Advanced", "Expert", "Specialist"]

# Hardcoded medical information
hardcoded_medical_info = """
  Advil, also known by its generic name ibuprofen, is a nonsteroidal anti-inflammatory drug (NSAID) commonly used to reduce pain, inflammation, and fever. It works by inhibiting the production of certain chemicals in the body that cause pain and inflammation.
Advil is available both over-the-counter and in prescription strength, depending on the dosage needed. This medication is commonly used to relieve various types of pain, including headache, toothache, menstrual cramps, muscle aches, back pain, and arthritis. It can also be used to reduce fever associated with common colds and flu. Advil is available in different forms, including tablets, liquid-filled capsules, and chewable tablets, allowing for flexibility in dosing and administration. While Advil can provide effective pain relief, it's important to use it responsibly and follow the recommended dosage instructions. Taking more than the recommended dose or using it for extended periods can increase the risk of side effects and potential complications. It's always advisable to consult with a healthcare professional before starting any new medication, including Advil, especially if you have pre-existing medical conditions or take other medications.
   As with any medication, Advil carries some potential side effects and precautions. Common side effects may include upset stomach, heartburn, dizziness, and drowsiness. These side effects are usually mild and temporary. However, if you experience severe or persistent side effects, it's important to seek medical attention.
Advil is generally well-tolerated by most people when used as directed. However, certain individuals may be at higher risk of experiencing adverse effects. It's important to avoid taking Advil if you are allergic to ibuprofen or other NSAIDs, or if you have a history of asthma, stomach ulcers, bleeding disorders, or kidney or liver problems. Additionally, Advil may interact with other medications, including blood thinners, certain antidepressants, and diuretics. It's crucial to inform your healthcare provider about all the medications and supplements you are taking to avoid potential drug interactions. It's worth noting that while Advil is commonly used for pain relief, it does not treat the underlying cause of the pain. If your symptoms persist or worsen, it's advisable to consult a healthcare professional for a proper diagnosis and comprehensive treatment plan.
"""

if "summary" not in st.session_state:
    st.session_state["summary"] = ""


st.title("Text Summarizer")

# Dropdown for knowledge level options
selected_knowledge_level = st.selectbox("Select your knowledge level:", knowledge_level_options)

st.text_area(label="Advil Information", value=hardcoded_medical_info, height=250)


##change
# "Submit" button  generate summary at the selected knowledge level
if st.button(
    "Submit",
    on_click=summarize,
    kwargs={"prompt": hardcoded_medical_info, "knowledge_level": selected_knowledge_level},
):
    st.session_state["summary"] = st.session_state["summary"]

output_text = st.text_area(label="Summarized text:", value=st.session_state["summary"], height=250)
