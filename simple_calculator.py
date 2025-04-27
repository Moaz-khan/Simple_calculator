import streamlit as st

# title
st.title("Simple Calculator")

# input

num1 = st.number_input("Enter first number")
num2 = st.number_input("Enter second number")

# operation
operation = st.selectbox("Select operation", ["Add", "Subtract", "Multiply", "Divide"])

# calculate
if st.button("Calculate"):
    if operation == "Additon":
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
        

# output
st.write(f"The result of {num1} {operation} {num2} is {result}") 

# Footer
st.footer("Developed by @Muhammad Maaz")


