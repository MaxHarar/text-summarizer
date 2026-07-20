# Medical Text Summarizer

A Streamlit app that takes dense medical text and explains it at the level of the person reading it. Pick one of five knowledge levels, from beginner to specialist, and the same source text comes back as a summary written for that reader.

Built during my summer as a Technology Intern at Johnson & Johnson (Titusville, NJ, 2023) to demonstrate an NLP use case for clinical documentation: medical information is written once, by experts, but read by patients, nurses, students, and physicians who all need different depth. One model plus five prompt templates covers the whole range.

## What it does

- Paste any medical text into the app (or run the built-in demo, which uses drug information for Advil)
- Choose a knowledge level: beginner, intermediate, advanced, expert, or specialist
- The app selects a prompt template matched to that level and sends it to GPT-3.5 Turbo on Azure OpenAI
- The summary comes back in the same UI, written for that reader

The interesting part is the prompt design, not the model call. A beginner gets "explain this in simple terms and define any complex medical words." A specialist gets "delve into the specifics as if explaining to a specialist." Same input, five different outputs, each one useful to a different person. In 2023, before this pattern had a name, that was the demo: audience-adaptive summarization as a prompting problem.

## How it's built

| File | What it does |
|------|--------------|
| `app.py` | Main Streamlit UI: free-text input, knowledge-level dropdown, summary output |
| `text_summarizer/functions.py` | The core: one prompt template per knowledge level, plus the chat completion call |
| `dynLang.py` | Azure OpenAI variant with `.env` config and the hardcoded Advil demo text |
| `getTokens.py` | tiktoken utility for counting tokens before sending a request |

Stack: Python, Streamlit, Azure OpenAI (GPT-3.5 Turbo), tiktoken.

## Run it

```bash
pip install streamlit "openai<1.0" python-dotenv tiktoken
```

The code uses the legacy `openai.ChatCompletion` API, so it needs an openai version below 1.0.

Copy the example env file and fill in your key (both entry points read from it):

```bash
cp .env.example .env
```

Then:

```bash
streamlit run dynLang.py   # Advil demo, Azure OpenAI config from .env
streamlit run app.py       # free-text input, key from .env
```

## Context

This was a 2023 internship demo and the code reflects it: small, direct, one idea executed clearly. The pattern it demonstrates, matching AI output to the audience reading it, is the same one I still build with today.

More of my work: [maxharar.com](https://maxharar.com)
