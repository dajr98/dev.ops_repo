import streamlit as st

# Title
st.title("💰 Tip Calculator")

st.write("Welcome to the tip calculator! Hopefully, you have your wallet. This program does not condone dining and dashing!")

# Data Gathering
bill = st.number_input("What was the total cost of everything?", min_value=0.0, format="%.2f")
tip = st.slider("What percentage of tip would you like to give?", 10, 20, 15)  # Slider for tip selection
people = st.number_input("How many people are splitting the bill?", min_value=1, step=1)

# Calculate the split
if people > 0:
    tip_as_percent = tip / 100
    total_tip_amount = bill * tip_as_percent
    total_bill = bill + total_tip_amount
    bill_per_person = total_bill / people
    final_amount = round(bill_per_person, 2)

    # Display results
    st.subheader("💵 Payment Breakdown")
    st.write(f"Total Bill (including tip): **${total_bill:.2f}**")
    st.write(f"Each person should pay: **${final_amount:.2f}**")

st.write("Thank you for using my invention. Remember to never dine and dash.")
st.write("Created by Zero Cool.")
