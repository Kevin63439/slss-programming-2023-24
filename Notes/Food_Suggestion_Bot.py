# Food Suggestion Bot
# Author : Kevin Wong
# 6 October 2023

# A bot that tasks the user what their favourie
# food is. Based on that food, it will classify
# the type/genre/cuisine of the food, then 
# give a restaurant suggestion.

import random
import time

# Introduce the bot to the user
# Ask the user what their favourite food is
print("Hello, I am here to suggest you a restaurant.")
time.sleep(1)
fave_food = input("To help me suggest a restaurant, what is your favourite food?").lower().strip(".,!?") 


# Italian Cuisine
italian_food = ["pasta", "pizza", "canneloni", "tiramisu"]
# Add another cuisine taht our bot should make a suggestion for
# Japanese cuisine:
japanese_food = ["sushi","ramen","udon","katsu"]
if fave_food.lower().strip("!.,?") in japanese_food:
    print("OH cool you might like Japanese food")
    time.sleep(1)
    print("You may like Suika")
    time.sleep(1)
    print("Here's their address 1626 W Broadway, Vancouver, BC V6J 1X6")
elif fave_food.lower().strip("!.,?") in italian_food:
    print("I see that you might like Italian food")
    time.sleep(1)
    print("Here's their address")
    time.sleep(1)
    print("186-8180 No 2 Rd, Richmond, BC")
else:
    print("I don't know what kind of food that is")
    time.sleep(1)
    print("I can't unfortunately recommend a restaurant")





