import streamlit as st
# Custom CSS to inject
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
def binary_search(low, high):
    return (low + high) // 2

def main():
    st.title("Machine Guessing Game")
    st.write("Think a number between 1 and 100 and I'll try to guess it!")

    # Initialize variables
    if 'low' not in st.session_state:
        st.session_state.low = 1
        st.session_state.high = 100
        st.session_state.attempts = 0
        st.session_state.guess = binary_search(st.session_state.low, st.session_state.high)
    
    # Display the current guess
    st.write(f"My last guess is: {st.session_state.guess}")

    # User feedback
    feedback = st.radio("Is my guess too high, too low, or correct?", 
                        ("Too High", "Too Low", "Correct"))
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if feedback == "Too High":
            st.session_state.high = st.session_state.guess - 1
        elif feedback == "Too Low":
            st.session_state.low = st.session_state.guess + 1
        elif feedback == "Correct":
            st.success(f"Yay! I guessed your number! in {st.session_state.attempts} atempts!! :raised_hands:")
            st.session_state.clear()  # Reset the game
            return

    # Make a new guess
    if feedback in ["Too High", "Too Low"]:
        st.session_state.guess = binary_search(st.session_state.low, st.session_state.high)

    
    # Display the updated guess
    st.write(f"My new guess is: {st.session_state.guess}")

if __name__ ==  "__main__":
    main() 