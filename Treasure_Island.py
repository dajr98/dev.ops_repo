import streamlit as st

st.title("Welcome to Treasure Island")
st.write('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
st.write("Your mission is to find the hidden treasure.")

choice1 = st.radio('You\'ve come to a crossroad with two choices. Which way would you like to go?',
                  ('left', 'right'))

if choice1 == "left":
    choice2 = st.radio('You\'ve come to a lake. Do you want to swim across or wait for a ferryman?',
                       ('swim', 'wait'))

    if choice2 == "wait":
        choice3 = st.radio('A ferryman stops by after a while. Will you board his boat?', ('yes', 'no'))
        if choice3 == "yes":
            choice4 = st.radio("You arrive at the island unharmed. You stumble across 3 doors. "
                               "One red, one yellow, and one blue. Which door would you like to choose?",
                               ('red', 'yellow', 'blue'))
            if choice4 == "red":
                st.write("Wrong door! A horde of Zombies attack and consume you... Sorry...")
            elif choice4 == "yellow":
                st.write("Wrong door! A bunch of Cobras attack and poison you with their venom. Game Over.")
            elif choice4 == "blue":
                st.write("Nice choice. You open the door and discover a room full of gold. You hit the jackpot!")
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
