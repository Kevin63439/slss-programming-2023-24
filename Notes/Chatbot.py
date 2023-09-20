# Chatbot
# Author: Ubial
# Date: 20 September 2023

# Greet the user
print("Hello there!")
# Get the user's name and store it in a variable
user_name = input("So... What's your name? ")

# Respond with the user's name in a friendly way
print(f"It's good to meet you,{user_name}.")

# Ask the user what their favourite food is
fave_food=input(f"So, {user_name}, what is your favourite food?")
# Make a comment about their food


# Make the comment about their favourite food but NOT BE TERRIBLY REPETITIVE
# Create a list of possible outcomes
list_of_responses=[f"Oh I have never tasted {fave_food} before.",
                   f"Cool I've never had {fave_food} before.",
                   f"I dont like {fave_food} anymore.",
                   f"I want some {fave_food} now."]

# Choose on of those responses randomly
import random
random_food_response = random.choice(list_of_responses)

# Print out that chosen response
print(random_food_response)