# This is a band name generator based the users input

st.write("Hello, welcome to the band naming generator! A simple yet cool way to come up with an original band name.")
city = st.text_input("Which city did you grow up in?\n")
pet = st.text_input("What is your pets name?\n")
color = st.text_input("What is your favorite color?\n")
st.write("Your potential band name could be", city + " " + pet + " " + color)





