# This is a band name generator based the users input

import streamlit as st

st.write("Hello, welcome to the funky naming generator! A simple yet cool way to come up with a fun and unique name.")
city = st.text_input("Which city did you grow up in?\n")
pet = st.text_input("What is your pets name?\n")
color = st.text_input("What is your favorite color?\n")
st.write("Your potential funky name could be", city + " " + pet + " " + color)





