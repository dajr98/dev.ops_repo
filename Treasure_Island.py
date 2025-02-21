import streamlit as st
import random

# Display a simple title instead of ASCII art
st.title("Welcome to Treasure Island")
st.write("Your mission is to find the hidden treasure.")

# Let the user select the first choice (left or right)
choice1 = st.radio("You come to a crossroad. Which way would you like to go?", ("left", "right"))

if choice1 == "left":
    choice2 = st.radio("You come to a lake. Type 'swim' to swim across, or 'wait' to wait for the ferryman.", ("swim", "wait"))

    if choice2 == "wait":
        choice3 = st.radio("A ferryman stops by. Will you board his boat?", ("yes", "no"))
        if choice3 == "yes":
            choice4 = st.radio("You arrive at the island. There are 3 doors: red, yellow, and blue. Which door would you like to choose?", ("red", "yellow", "blue"))
            if choice4 == "red":
                st.write("Wrong door! A horde of Zombies attack and consume you... Sorry...")
            elif choice4 == "yellow":
                st.write("Wrong door! A bunch of Cobras attack and poison you with their venom. Game Over.")
            elif choice4 == "blue":
                st.write("Nice choice! You open the door and discover a room full of gold. You hit the jackpot!")
            else:
                st.write("Not quite. You fell into a magical bottomless pit. Game Over.")
        else:
            st.write("You refuse to board the ferryman's boat. You die of dehydration. Game Over.")
    elif choice2 == "swim":
        st.write("You get devoured by sharks. Sorry...")
    else:
        st.write("Not quite. You fall down some trap doors!")
else:
    st.write("Not quite. You fall down some trap doors!")

st.write("Thanks for playing!")
