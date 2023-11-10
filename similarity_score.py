# Comparing Similarity Scores
# Author: Kevin Wong
# 8 November 2023

# Calculate similarity scores between 2 people

# Create two lists that represent the movies 
# that people like
kevins_favourite_movies = [
    "Black Panther",
    "Five Nights at Freddies",
    "John Wick 2",
    "Cars 2",
    "2 Fast 2 Furious"
]
matts_favourite_movies = [
    "spider_man: Into the spider verse",
    "John Wick 2",
    "Equalizer",
    "Infinity War",
    "Forest Gump"
]
# Initialize the similarity score

similarity_score = 0

# Iterate through all movies in first list
for movie in kevins_favourite_movies: 
    if movie in matts_favourite_movies:
        similarity_score += 1

# Display the results
print(f"Kevin and Matt have a similarity score of {similarity_score}.")