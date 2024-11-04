import streamlit as st
from load_data import load_data

def terminal_glossary():
    data = load_data()
    terminal_questions = data.get("quiz", {}).get("terminal", [])

    # Initialize session state variables if they don't exist
    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.submitted = False
        st.session_state.selected_answer = None

    # Total number of questions
    total_questions = len(terminal_questions)
    current_question = st.session_state.question_index + 1  # +1 to make it 1-based index

    # Display current question and total number of questions
    st.write(f"Question {current_question} of {total_questions}")

    # Visual progress bar
    progress = (st.session_state.question_index + 1) / total_questions  # Calculate progress as a fraction
    st.progress(progress)  # Create a progress bar

    # Check if there are questions left
    if st.session_state.question_index < total_questions:
        item = terminal_questions[st.session_state.question_index]
        st.write(f"Question: {item['question']}")

        # Radio button for answers
        answer = st.radio("Select your answer: ", item["options"], key=f"radio_{st.session_state.question_index}",
                          index=0 if st.session_state.selected_answer is None else item["options"].index(st.session_state.selected_answer))

        # Store the selected answer
        st.session_state.selected_answer = answer

        # Submit button to check the answer
        if st.button("Submit", key=f"submit_{st.session_state.question_index}"):
            if answer is None:
                st.error("Please select an answer before submitting.")
            elif answer == item["correct_answer"]:
                st.success("Correct!")
                st.session_state.score += 1
            else:
                st.error("Incorrect. Try again.")
            
            st.session_state.submitted = True  # Mark as submitted

        # Show "Next" button
        if st.session_state.submitted:
            if st.button("Next", key=f"next_{st.session_state.question_index}"):
                st.session_state.question_index += 1  # Move to the next question
                st.session_state.submitted = False  # Reset submitted status for the next question
                st.session_state.selected_answer = None  # Reset selected answer for the next question

    else:
        # If there are no more questions
        st.write("Quiz Completed!")
        st.write(f"Your score: {st.session_state.score} out of {total_questions}")

        if st.button("Restart Quiz"):
            # Reset all session state variables
            st.session_state.question_index = 0
            st.session_state.score = 0
            st.session_state.submitted = False
            st.session_state.selected_answer = None
