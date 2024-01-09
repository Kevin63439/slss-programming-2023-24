# Winter Holidays
# Author: Kevin Wong
# 8 January 2024

# Requirements:
# - create a function called winter_holiday()
#   - takes one parameter - string
#   - returns a summary of an event from your holidays

# Please do not use ChatGPT or any LLM

import random

good = ("I ate lots of food!",
        "I played sports!",
        "I spent time with family and friends!",
        "I worked out!")

bad = ("I was supposed to ski but the weather was bad",
       "I was not productive with school work",
       "I was tired physically")

def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24
    
    Params:
        good_or_bad - string that indicates whether the event
            is good or bad
    
    Returns:
        an event that happened to you during the holidays
        the event is selected part"""
    
    if good_or_bad.strip(",.!?") == "good":
        return random.choice(good)
    else: 
        return random.choice(bad)

def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday(input("How was ur christmas break?")))
    # "I got a Lego set for the first time in a long time."
    # "I went to Richmond Centre to walk around aimlessly."
    # "I hoped to snowboard but then it was raining"


# If we're running THIS FILE using Python
if __name__ == "__main__":
    main() 