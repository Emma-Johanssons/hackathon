import streamlit as st

from Terminal_Glossary import terminal_glossary
from OOP import oop_glossary
from quiz import quiz_glossary

# @st.cache_data



st.title("Python Quiz")

st.sidebar.header("Quiz Category")
page = st.sidebar.selectbox(
    "Choose a category:", ["Terminal", "Object Oriented Programming", "Random Quiz"]
)


if page == "Terminal":
    st.subheader("Terminal - Glossary")
    terminal_glossary()

if page == "Object Oriented Programming":
    st.subheader("Object Oriented Programming - Glossary")
    oop_glossary()

if page == "Random Quiz":
    st.subheader("Random Quiz")
    quiz_glossary()