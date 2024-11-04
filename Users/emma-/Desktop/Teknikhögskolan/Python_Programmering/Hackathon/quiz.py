import streamlit as st
from load_data import load_data

def quiz_glossary():
    data = load_data()
    quiz_questions = data.get("quiz", {}).get("questions", [])

    # Initialize session state variables
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0

    # Total number of questions
    total_questions = len(quiz_questions)
    current_question = st.session_state.question_index + 1  # +1 to make it 1-based index

    # Display current question and total number of questions
    st.write(f"Question {current_question} of {total_questions}")

    # Visual progress bar
    progress = current_question / total_questions  # Calculate progress as a fraction
    st.progress(progress)  # Create a progress bar

    # Function to increment question index
    def increment_question():
        st.session_state.question_index += 1
        # Clear the form submission state
        if 'form_submitted' in st.session_state:
            del st.session_state.form_submitted

    if st.session_state.question_index < len(quiz_questions):
        item = quiz_questions[st.session_state.question_index]
        st.write(f"Question: {item['question']}")

        # Create a form for the question
        with st.form(key=f'quiz_form_{st.session_state.question_index}'):
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
        if 'form_submitted' in st.session_state:
            st.button('Next Question', on_click=increment_question, key=f'next_{st.session_state.question_index}')

    else:
        st.write("Quiz Completed!")
        st.write(f"Your score: {st.session_state.score} out of {len(quiz_questions)}")
        
        if st.button("Restart Quiz"):
            st.session_state.question_index = 0
            st.session_state.score = 0
            if 'form_submitted' in st.session_state:
                del st.session_state.form_submitted
