import streamlit as st
from riddles import load_riddles, get_random_riddle

# Loading CSS from file
def load_css(file_name):
    with open(file_name) as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    
load_css('css/style.css')

# Loading  riddles
riddles = load_riddles()

# Checking if riddles loaded
if not riddles:
    st.write("No riddles found. Please check your CSV file.")
else:
    # Initializing session state variables
    if "riddle" not in st.session_state:
        st.session_state.riddle = get_random_riddle(riddles)
        st.session_state.hint_shown = False
        st.session_state.answer_shown = False
        st.session_state.user_answer_key = 0  

    # Displaying the riddle
    st.header("Lets Riddle")
    st.write(st.session_state.riddle['Riddle'])
    

    # Users input
    user_answer = st.text_input("Your answer is :",placeholder="Type Your Answer Here", key=f"user_answer_{st.session_state.user_answer_key}")

    # Buttons submit , hint , reveal 
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Submit"):
            if user_answer.strip().lower() == st.session_state.riddle['Answer'].lower():
                st.write("Correct! Well done!")
            else:
                st.write("Incorrect, ask for a hint")
        
    with col2:
        if st.button("Hint"):
            if not st.session_state.hint_shown:
                st.write(f"Hint:    {st.session_state.riddle['Hint']}")
                st.session_state.hint_shown = True
            else:
                st.write("Hint already shown.")

    with col3:
        if st.button("Reveal"):
            if not st.session_state.answer_shown:
                st.write(f"The answer is: {st.session_state.riddle['Answer']}")
                st.session_state.answer_shown = True
            else:
                st.write("Answer already revealed.")

    #Next riddle
    st.write("")  
    # Center the button by using a three-column layout
    col_center = st.columns([1, 1, 1])[1]  
    with col_center:
        if st.button("Next"):
            st.session_state.riddle = get_random_riddle(riddles)
            st.session_state.hint_shown = False
            st.session_state.answer_shown = False
            st.session_state.user_answer_key += 1  # Increment key to reset input
            st.rerun()
