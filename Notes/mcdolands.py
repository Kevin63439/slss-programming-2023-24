# Mcdolands bot
# Author: Kevin Wong
# 3 November 2023

# CONSTS
TAX =0.14
BURGER_COST =5
FRIES =3

cost = 0
# Ask the user what they want

burger_yes = input("Would you like a burger for $5? (Yes/No)").lower().strip("!?,.")
if burger_yes == "yes":
    cost += BURGER_COST

fries_yes = input("Would you like fries for $3? (Yes/No)").lower().strip("!.,?")
if fries_yes == "yes":
    cost += FRIES

final_cost = cost*(1+TAX)
print(f"Your total is ${final_cost:.2f}")
