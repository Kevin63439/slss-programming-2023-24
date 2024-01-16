# Spotify Data Analyzer
# Kevin Wong
# January 16 2024

import csv

# Open the file
with open("./spotify.csv") as f:


    # ---- Search for all Drake Songs
    # ---- Use linear search
    # Create a csv reader object
    csv_reader = csv.DictReader(f)

    # Make a list to store all Drake songs
    drake_songs = []

    # Create a counter to store the current line number
    line_num == 0 

    # For every line in the file
    for line in csv.reader:
        # If it's the first line, print out all the headings
        if line_num == 0:
            print("The columns are:") 
            for item in line:
                 print(item)

        # If the artist for this song is Drake
            # Store the song info in the list
            # ---- artist, song title. danceability