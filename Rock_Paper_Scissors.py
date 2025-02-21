Rock_Paper_Scissors


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
import random
game_images = [rock, paper, scissors]

user_choice = int(input("Make your choice... Choose 0 for Rock. 1 for Paper. Or 2 for Scissors."))

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("The computer chose:")
print(game_images[computer_choice])

if user_choice >=3 or user_choice < 0:
    print("That wasn't an option! You lose. :( ")

elif user_choice == 0 and computer_choice == 2:
    print("You won!")

elif user_choice == 2 and computer_choice == 0:
    print("Sorry. You lost!")
elif computer_choice > user_choice:
    print("Sorry. You lost!")
elif user_choice > computer_choice:
    print("Nice move! You won!")
elif computer_choice == user_choice:
    print("It's a stalemate!")







