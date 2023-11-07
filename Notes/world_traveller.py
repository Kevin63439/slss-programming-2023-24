# World traveller bot
# Author: Kevin Wong
# 6 November 2023

# Greet the user
your_name = input(f"Hi my friend what's your name?")

print(f"What's good {your_name}? It's great to meet you! I will be determining how many continents you've been to.")

# Country questions

continents_list = ["Asia", "Europe", "North America", "South America", "Australia", "Africa", "Antarctica"]

places = 0

for continents in continents_list:
    continents_yes = input(f"Have you been to {continents}? (Yes/No)").lower().strip("!?,.")
    if continents_yes == "yes":
        places += 1

# Score
print(f"I see {your_name}, you've visited {places}/7 continents!")