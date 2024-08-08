'''
Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?

In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).
'''

def main():
    # prompts the user for a time
    prompt = input("What's the time? ")
    # time is assigned the value retrieved from calling convert with the value from prompt passed to it. Here we jump down to convert function 👇
    time = convert(prompt)

    # With that value from time we check the meal time
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif  time >= 12 and time <= 13:
        print("lunch time")
    elif  time >= 18 and time <= 19:
        print("dinner time")

def convert(time):                          #ie 7:30 from prompt
    hour,minute = time.split(":")           # splits to strings of "7","30"
    float_min = float(minute) / 60          # "30" becomes float 0.5
    return float(hour) + float_min          # returns 7.5


if __name__ == "__main__":
    main()