# Loop Practice
# Author: Kevin Wong
# Date: 10 October 2023

# Create a list of groceries
groceries = ["hot wheels", "lego", "ice cream", "video games"]

# Do something for each thing in the list
# Print it out in a pretty way
# e.g.
#   - hotwheels
#   ———
#   - lego
#   ---
#   - etc.

# print(f'.{groceries[0]})
#print ('---')
# print(f'.{groceries[1]})
#print ('---')
# print(f'.{groceries[2]})
#print ('---')

for item in groceries:
    print(f"* {item}")
    print(f" ---")

# Using the above method, create the thing below:
# *
# **
# ***
# ****
# *****
# ******

pyramid = ["*", "**", "***", "****", "*****", "******"]

for row in pyramid:
    print(f" {row}")

# Problem;
# Create a New Years Countdown that's automated
# starts at 10
# counts down every second printing the second its at
# instead of reaching zero, it prints out "Happy New Year"

import time

new_year = ["10", "9", "8", "7", "6", "5","4", "3", "2", "1", "Happy New Year!!@!" ]

for countdown in new_year:
    print(f" {countdown}")
    time.sleep(1)