import streamlit as st
from Terminal_Glossary import terminal_glossary
from OOP import oop_glossary
from quiz import quiz_glossary
from pandas_glossary import pandas_glossary
from git_glossary import git_glossary
import openai
from dotenv import load_dotenv
import os


load_dotenv()
openai.api_key = os.getenv("OPEN_AI_KEY")
def generate_explanation(question, correct_answer):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Explain why '{correct_answer}' is the correct answer to the question: '{question}'",
            max_tokens=100,
            temperature=0.5
        )
        explanation = response.choices[0].text.strip()
        return explanation
    except Exception:
        return "Could not generate an explanation."




st.title("Python Quiz")

st.sidebar.header("Quiz Category")
page = st.sidebar.selectbox(
    "Choose a category:", ["Terminal", "Git", "Object Oriented Programming", "Random Quiz", "Pandas",]
)

# Reset session state if a new page is selected
if "current_page" not in st.session_state or st.session_state.current_page != page:
    # Resetting only the quiz-related session state variables
    if page == "Terminal":
        st.session_state.pop("question_index", None)
        st.session_state.pop("score", None)
        st.session_state.pop("form_submitted", None)
    elif page == "Git":
        st.session_state.pop("question_index", None)
        st.session_state.pop("score", None)
        st.session_state.pop("form_submitted", None)
    elif page == "Object Oriented Programming":
        st.session_state.pop("question_index", None)
        st.session_state.pop("score", None)
        st.session_state.pop("form_submitted", None)
    elif page == "Random Quiz":
        st.session_state.pop("question_index", None)
        st.session_state.pop("score", None)
        st.session_state.pop("form_submitted", None)
    elif page == "Pandas":
        st.session_state.pop("question_index", None)
        st.session_state.pop("score", None)
        st.session_state.pop("form_submitted", None)
    

    # Update current page in session state
    st.session_state.current_page = page

if page == "Terminal":
    st.subheader("Terminal - Glossary")
    terminal_glossary()
elif page == "Git":
    st.subheader("Git - Glossary")
    git_glossary()
elif page == "Object Oriented Programming":
    st.subheader("Object Oriented Programming - Glossary")
    oop_glossary()

elif page == "Random Quiz":
    st.subheader("Random Quiz")
    quiz_glossary()

elif page == "Pandas":
    st.subheader("Pandas - Glossary")
    pandas_glossary()