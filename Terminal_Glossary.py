

        

import random  # Import random to use for shuffling
from load_data import load_data
import streamlit as st
import openai  # Import OpenAI for using the API
import os
from dotenv import load_dotenv  # To load environment variables

# Load environment variables from .env
load_dotenv()
openai.api_key = os.getenv("OPEN_AI_KEY")  # Set your OpenAI API key

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

def terminal_glossary():
    data = load_data()
    terminal_questions = data.get("quiz", {}).get("terminal", [])

    # Shuffle the questions at the start of the quiz
    random.shuffle(terminal_questions)

    # Shuffle the options for each question
    for question in terminal_questions:
        random.shuffle(question["options"])

    # Initialize session state variables if they don't exist
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.form_submitted = False
        st.session_state.explanation = ""  # To hold AI explanation

    # Total number of questions
    total_questions = len(terminal_questions)
    current_question = st.session_state.question_index + 1  # +1 to make it 1-based index

    # Display current question and total number of questions if the quiz is not completed
    if st.session_state.question_index < total_questions:
        st.write(f"Question {current_question} of {total_questions}")

        # Visual progress bar
        if total_questions > 0:  # Prevent division by zero
            progress = min(current_question / total_questions, 1.0)  # Clamp the progress value to 1.0
            st.progress(progress)  # Create a progress bar

        # Function to increment question index
        def increment_question():
            st.session_state.question_index += 1
            st.session_state.form_submitted = False  # Reset form submission status
            st.session_state.explanation = ""  # Reset explanation for next question

        item = terminal_questions[st.session_state.question_index]
        st.write(f"Question: {item['question']}")

        # Create a form for the question
        with st.form(key=f'oop_quiz_form_{st.session_state.question_index}'):
            answer = st.radio(
                "Select your answer: ",
                item["options"],
                key=f"radio_{st.session_state.question_index}"
            )
            
            # Submit form button
            submitted = st.form_submit_button("Submit")
            
            if submitted:
                st.session_state.form_submitted = True
                if answer == item["correct_answer"]:
                    st.session_state.score += 1
                    st.success("Correct!")
                else:
                    st.error(f"Incorrect. The correct answer was: {item['correct_answer']}")
                    st.session_state.explanation = generate_explanation(item["question"], item["correct_answer"])
                    st.write("**Explanation:**")
                    st.write(st.session_state.explanation)
                                

        # Only show Next button after form is submitted and explanation has been shown
        if st.session_state.form_submitted:
                st.button('Next Question', on_click=increment_question, key=f'next_{st.session_state.question_index}')

        

    else:
        # Quiz Completed
        st.write("Quiz Completed!")
        st.write(f"Your score: {st.session_state.score} out of {total_questions}")


