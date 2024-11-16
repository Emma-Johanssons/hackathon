import streamlit as st
import random  # Import random to use for shuffling
from load_data import load_data

def pandas_glossary():
    data = load_data()
    pandas_questions = data.get("quiz", {}).get("pandas", [])

    # Shuffle the questions at the start of the quiz
    random.shuffle(pandas_questions)

    # Shuffle the options for each question
    for question in pandas_questions:
        random.shuffle(question["options"])

    # Initialize session state variables if they don't exist
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.form_submitted = False

    # Total number of questions
    total_questions = len(pandas_questions)
    current_question = st.session_state.question_index + 1  # +1 to make it 1-based index

    # Display current question and total number of questions if the quiz is not completed
    if st.session_state.question_index < total_questions:
        st.write(f"Question {current_question} of {total_questions}")

        # Visual progress bar
        if total_questions > 0:  # Prevent division by zero
            progress = min(current_question / total_questions, 1.0)  # Clamp the progress value to 1.0
            st.progress(progress)  # Create a progress bar

        item = pandas_questions[st.session_state.question_index]
        st.write(f"Question: {item['question']}")

        # Create a form for the question
        with st.form(key=f'pandas_quiz_form_{st.session_state.question_index}'):
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

        # Only show Next button after form is submitted
        if st.session_state.form_submitted:
            st.button('Next Question', on_click=lambda: st.session_state.update({'question_index': st.session_state.question_index + 1, 'form_submitted': False}), key=f'next_{st.session_state.question_index}')

    else:
        # Quiz Completed
        st.write("Quiz Completed!")
        st.write(f"Your score: {st.session_state.score} out of {total_questions}")

