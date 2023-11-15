# Parental bot
# Author: Kevin Wong
# November 14 2023

# Greet the user
print("Hi there I'm a parental bot that will see how good you are.")

# Make list with questions
questions = [
    "Did you eat?",
    "Did you study?",
    "Did you do your laundry?",
    "Did you call grandma?"

]

# Initialize score
number_yes = 0

# Get scores
for question in questions:
    if input(question).strip(",.?!").lower()=="yes":
        number_yes += 1

# Print response based on number of yes
if number_yes == 0:
    print("I'm coming over!!")
elif 1 > number_yes > 2:
    print("Ok") 
else:
    print("That's good!")

