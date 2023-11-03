# Olympic judging
# Author: Kevin Wong
# 3 November 2023

# Greet the User
print("Hi this is an Olympic Judging program. Input your 5 scores!")

numbers=['first','second','third','fourth','fifth']

scores=0

# Ask user their 5 scores
for number in numbers:
    scores+=float(input(f"What is your {number} score on a scale from 1-10? 1 being atrocious and 10 being perfection!"))

# Math part
print(f"Your Olympic score is: {scores /5 :.2f} ")

