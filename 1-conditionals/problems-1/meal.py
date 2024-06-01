"""
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
"""

# implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all

def main():
# Get time from user
    time = input("What is the time? ")
# Call the convert function to convert the time
    converted_time = convert(time)
# Breakfast between 7:00 & 8:00
    if converted_time >= 7 and converted_time <= 8:
        print("breakfast time")
# Lunch between 12:00 & 13:00
    elif converted_time >= 12 and converted_time <= 13:
        print("lunch time")
# Dinner between 18:00 & 19:00
    elif converted_time >= 18 and converted_time <= 19:
        print("dinner time")
    else:
        print("not time for a meal")

def convert(time):
    # Get hour and minute
    hour, minute  = time.split(":")
    # Convert time to a float
    converted_minutes = float(minute) / 60
    # Return the result to main()
    return float(hour) + converted_minutes


if __name__ == "__main__":
    main()