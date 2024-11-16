import streamlit as st
import random

st.markdown("""
<style>
.streamlit-container {
    border: 2px solid #000;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)
col1, col2= st.columns(2)
with col1:
    st.write("IPS Tech Community")
with col2:
    st.write("PyEXPO'25")

def guessing_game():
    st.title("Number Guessing Game")

    # Initialize session state variables
    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

    # User input for guessing
    guess = st.slider("Guess a number between 1 and 100:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.markdown("Too low! Try again.")
        elif guess > st.session_state.number:
            st.markdown("Too high! Try again.")
        elif guess== st.session_state.number:
            st.success(f":tada: Congratulations!You have guessed the number correctly in {st.session_state.attempts} attempts...!	:tada:")
            # Reset game
            if st.button("Play Again...!?"):
                st.session_state.number = random.randint(1, 100)
                st.session_state.attempts = 0
                

if __name__ == "__main__":
    guessing_game()