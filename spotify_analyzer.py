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
    line_num = 0 

    # For every line in the file
    for line in csv_reader:
        # If it's the first line, print out all the headings
        if line_num == 0:
            print("The columns are:") 
            
            print(", ".join(line))

            # Print one on every line
            # For item in line:
            #   print(item)

            line_num += 1
        else:

        # If the artist for this song is Drake
            # Store the song info in the list
            # ---- artist, song title. danceability
            if "drake" in line["artist"].lower():
                drake_songs.append((
                    line["artist"],
                    line["song_title"],
                    line["danceability"]
                ))
            line_num += 1

# Print only the drake songs 
# that have a danceability of .5 or higher
for song in drake_songs:
    if float(song[2]) >= .5:
        print(song[1])
