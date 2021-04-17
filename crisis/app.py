from datetime import datetime

import streamlit as st
import openai

st.title("Crisis on Infinite Tweets")


st.sidebar.write("Settings")
openai_key = st.sidebar.text_input("OpenAI API key", type="password")
openai.api_key = openai_key
engines = openai.Engine.list()
engine_ids = [e["id"] for e in engines["data"]]

engine = st.sidebar.selectbox(
    "Model engine",
    options=engine_ids,
    index=(engine_ids.index("davinci") if "davinci" in engine_ids else 0),
)

n_answers = st.sidebar.slider(
    "Number of answers to generate", min_value=1, max_value=5, step=1, value=1
)
temperature = st.sidebar.slider(
    "Model temperature", min_value=0.0, max_value=1.0, step=0.05, value=0.15
)
max_tokens = st.sidebar.slider(
    "Maximal answer length", min_value=1, max_value=512, value=256
)


"""Search RSS feeds and summarize info through GPT-3!"""
st.selectbox("What topic interests you?", options=["foo", "bar", "gpt-3"])
search_phrase = st.text_area("What question do you want to ask GPT-3?")

submit_button = st.button("Submit")

if submit_button:
    f"""{datetime.now()}"""
    """Submitted!"""


else:
    """Press submit!"""