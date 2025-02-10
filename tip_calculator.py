# Tip Calculator

print("Welcome to the tip calculator! Hopefully you have your wallet. This program does not condone dining and dashing!")

#Data Gathering
bill = float(input("What was the total cost of everything? \n$"))
tip = (int(input("What percentage of tip would you like to give?\n 10p 12p 15p 20p\n")))
people = int(input("How many people are going to split the bill?\n"))

#Equations
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"To make it equal, each person should pay {final_amount}")
print("Thank you for using my invention. Remember to never dine and dash.")
print("Created by Zero Cool.")