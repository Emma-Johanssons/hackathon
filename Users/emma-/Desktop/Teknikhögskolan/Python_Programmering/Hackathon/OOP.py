import streamlit as st
from load_data import load_data

def oop_glossary():
    data = load_data()
    oop_questions = data.get("quiz", {}).get("object_oriented_programming", [])

    # Initialize session state variables
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answer_submitted = False  # Initialize answer_submitted

    # Total number of questions
    total_questions = len(oop_questions)
    current_question = st.session_state.question_index + 1  # +1 to make it 1-based index

    # Display current question and total number of questions
    st.write(f"Question {current_question} of {total_questions}")

    # Visual progress bar
    progress = current_question / total_questions  # Calculate progress as a fraction
    st.progress(progress)  # Create a progress bar

    # Ensure we only display questions if we haven't completed the quiz
    if st.session_state.question_index < total_questions:
        item = oop_questions[st.session_state.question_index]
        st.write(f"Question: {item['question']}")

        answer = st.radio("Select your answer: ", item["options"], key=f"radio_{st.session_state.question_index}")

        # Submission Button
        if st.button("Submit", key=f"submit_{st.session_state.question_index}"):
            # Check if an answer was selected
            if answer is None:
                st.error("Please select an answer before submitting.")
            else:
                # Check if the answer is correct
                if answer == item["correct_answer"]:
                    st.success("Correct!")
                    st.session_state.score += 1
                else:
                    st.error(f"Incorrect. The correct answer was: {item['correct_answer']}")

                st.session_state.answer_submitted = True  # Mark that the answer has been submitted

    # Submission Button and Navigation
    if st.session_state.answer_submitted:
        if st.session_state.question_index < total_questions - 1:
            if st.button('Next Question'):
                st.session_state.question_index += 1  # Move to the next question
                st.session_state.answer_submitted = False  # Reset submission state for the next question
        else:
            # If all questions are answered
            st.write("Quiz Completed!")
            st.write(f"Your score: {st.session_state.score} out of {len(oop_questions)}")
            if st.button('Restart Quiz'):
                st.session_state.question_index = 0
                st.session_state.score = 0
                st.session_state.answer_submitted = False  # Reset for a new quiz
    else:
        if st.session_state.question_index < total_questions:
            st.button('Submit', key=f"submit_button_{st.session_state.question_index}")
