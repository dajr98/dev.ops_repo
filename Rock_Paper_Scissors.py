import streamlit as st
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

st.title("Rock Paper Scissors Game")

# Let the user select their choice using radio buttons
user_choice = st.radio("Make your choice... Choose 0 for Rock, 1 for Paper, or 2 for Scissors.", (0, 1, 2))

# Display the ASCII art of the user's choice
st.write("You chose:")
st.text(game_images[user_choice])

# Generate the computer's choice
computer_choice = random.randint(0, 2)
st.write("The computer chose:")
st.text(game_images[computer_choice])

# Determine and display the result of the game
if user_choice == computer_choice:
    st.write("It's a stalemate!")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    st.write("You won!")
else:
    st.write("Sorry. You lost!")
