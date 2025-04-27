import streamlit as st

# Title
st.title("Simple Calculator")

# Inputs
num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

# Operation selection
operation = st.selectbox(
    "Choose operation", 
    ("Addition", "Subtraction", "Multiplication", "Division", "Percentage")
)

# Button
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero!"
    elif operation == "Percentage":
        if num2 != 0:
            result = (num1 / num2) * 100
        else:
            result = "Cannot calculate percentage with denominator 0!"

    st.success(f"Result: {result}")

# Footer
st.footer("Developed by @Muhammad Maaz")


