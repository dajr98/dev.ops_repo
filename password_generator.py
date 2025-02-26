import streamlit as st
import random

# List of characters for password generation
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

# Streamlit UI
st.title("🔑 Secret Python Password Generator")

# User input fields
number_letters = st.number_input("How many letters would you like in your password?", min_value=1, step=1, value=4)
number_symbols = st.number_input("How many symbols would you like to add?", min_value=0, step=1, value=2)
number_numbers = st.number_input("How many numbers would you like to add?", min_value=0, step=1, value=2)

# Generate password on button click
if st.button("Generate Password"):
    password = "".join(random.choices(letters, k=number_letters)) + \
               "".join(random.choices(symbols, k=number_symbols)) + \
               "".join(random.choices(numbers, k=number_numbers))

    # Shuffle password characters
    password = ''.join(random.sample(password, len(password)))

    st.success(f"Your generated password: **{password}**")
