# Similar hobbies bot
# Author: Kevin Wong
# November 14 2023

# Greet User
print("Hello my friend I will calculate your similarity score between you and another person.")

person1_hobbies = input("So user 1 please enter 3 hobbies, separated by spaces.").lower().split()

person2_hobbies = input("So user 2 please enter 3 hobbies, separated by spaces.").lower().split()

# Initialize Similarity Score
similarity_score = 0

# Iterate through all movies in first list
for hobbies in person1_hobbies: 
    if hobbies in person2_hobbies:
        similarity_score += 1

# Display results
print(f"User 1 and User 2 have {similarity_score} hobbies in common!")
