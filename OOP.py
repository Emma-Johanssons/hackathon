import streamlit as st
import random  # Import random to use for shuffling
from load_data import load_data
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPEN_AI_KEY")

def generate_explanation(question, correct_answer):
    """Generates a more informative explanation for the correct answer using OpenAI's API."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=[
                {"role": "user", "content": f"Explain why '{correct_answer}' is the correct answer to the question: '{question}'. Provide a brief but informative explanation suitable for students learning Python."}
            ],
            max_tokens=150,  # Allow for a slightly longer response
            temperature=0.5
        )
        explanation = response.choices[0].message['content'].strip()
        return explanation
    except Exception as e:
        return f"Could not generate an explanation. Error: {str(e)}"

def oop_glossary():
    data = load_data()
    oop_questions = data.get("quiz", {}).get("object_oriented_programming", [])
    random.shuffle(oop_questions)  # Shuffle questions

    # Initialize session state variables if they don't exist
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.form_submitted = False
        st.session_state.explanation = ""  # För att hålla AI-förklaringen
        st.session_state.show_explanation = False  # Flagga för att visa förklaringen

    total_questions = len(oop_questions)
    current_question = st.session_state.question_index + 1

    if st.session_state.question_index < total_questions:
        st.write(f"Question {current_question} of {total_questions}")
        st.progress(min(current_question / total_questions, 1.0))

        def increment_question():
            st.session_state.question_index += 1
            st.session_state.form_submitted = False
            st.session_state.explanation = ""  # Reset explanation for next question
            st.session_state.show_explanation = False  # Reset flag for showing explanation

        item = oop_questions[st.session_state.question_index]
        st.write(f"Question: {item['question']}")

        with st.form(key=f'quiz_form_{st.session_state.question_index}'):
            answer = st.radio("Select your answer: ", item["options"], key=f"radio_{st.session_state.question_index}")
            submitted = st.form_submit_button("Submit")

            if submitted:
                st.session_state.form_submitted = True
                if answer == item["correct_answer"]:
                    st.session_state.score += 1
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The correct answer was: {item['correct_answer']}")

                # Generate and display explanation
                st.session_state.explanation = generate_explanation(item["question"], item["correct_answer"])

        # Show a button to ask if the user wants to see the explanation
        if st.session_state.form_submitted:
            if st.button("Do you want to see the explanation for the correct answer?"):
                st.session_state.show_explanation = True  # Set flag to show explanation

            if st.session_state.show_explanation:
                st.write("**Explanation:**")
                st.write(st.session_state.explanation)

            st.button('Next Question', on_click=increment_question, key=f'next_{st.session_state.question_index}')

    else:
        st.write("Quiz Completed!")
        st.write(f"Your score: {st.session_state.score} out of {total_questions}")

