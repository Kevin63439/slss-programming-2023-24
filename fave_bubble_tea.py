# Bubble tea Popularity Algorithm
# Author: Kevin Wong
# Date: 27 October 2023

# Ask 5 users what their favourite bubble tea plac eis
# Prints out a summary of the data

# CONSTS
NUM_RESPONDENTS=5

# Like counters
coco_likes = 0      # Initialize the variable to 0
tang_likes = 0
suntea_likes = 0
chatime_likes = 0
bubqueen_likes = 0

for _ in range(NUM_RESPONDENTS):


    # Ask the user what their favourite place ishhgghg
    # Store that information somewhere
    print("What's your favourite bubble tea place?")

    fave_place = input().strip(",.?!").lower()

    # Tally or counting algo
    # Options: CoCo, Suntea, Chatime, Bubble Queen, Xing fu tang
    # If they choose any of these options, increase the counter
    if fave_place == "coco":
        coco_likes = coco_likes + 1
    elif fave_place == "suntea":
        suntea_likes += 1
    elif fave_place == "bubble queen":
        bubqueen_likes += 1
    elif fave_place == "chatime":
        chatime_likes += 1
    elif fave_place == "xing fu tang":
        tang_likes += 1

    # Repeat five times.

# Print out a summary

# Give the raw score AND the score as percentage
print(f"CoCo likes: {coco_likes}")
print(f"Bubble queen likes: {bubqueen_likes}")
print(f"Suntea likes: {suntea_likes}")
print(f"Xing fu tang likes: {tang_likes}")
print(f"Chatime likes: {chatime_likes}")

print(f"CoCo percentage: {round (coco_likes / NUM_RESPONDENTS * 100)}%")
print(f"Bubble queen likes: {round (bubqueen_likes / NUM_RESPONDENTS * 100)}%")
print(f"Suntea likes: {round (suntea_likes / NUM_RESPONDENTS * 100)}%")
print(f"Xing fu tang likes: {round (tang_likes / NUM_RESPONDENTS * 100)}%")
print(f"Chatime likes: {round (chatime_likes / NUM_RESPONDENTS * 100)}%")