import streamlit as st
from agent import generate_test_script

st.title("🤖 AI Test Script Generator")

# Inputs
steps = st.text_area("Enter Test Steps", height=150)
actual = st.text_input("Actual Value")
expected = st.text_input("Expected Value")

# Button
if st.button("Generate Script"):
    if steps.strip() == "":
        st.warning("Please enter test steps ⚠️")
    else:
        with st.spinner("Generating..."):
            output = generate_test_script(steps, actual, expected)

        st.success("Done ✅")
        st.code(output)