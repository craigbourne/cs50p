"""
In a file called nutrition.py, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., strawberries, not strawberry). Ignore any input that isn’t a fruit.
"""

# prompts consumers users to input a fruit
prompt = input("Item: ")

fruits = [{"Name": "Apple", "Calories": "130"},
          {"Name": "Avocado", "Calories": "50"},
          {"Name": "Banana", "Calories": "110"},
          {"Name": "Cantaloupe", "Calories": "50"},
          {"Name": "Grapefruit", "Calories": "60"},
          {"Name": "Grapes", "Calories": "90"},
          {"Name": "Honeydew", "Calories": "50"},
          {"Name": "Kiwifruit", "Calories": "90"},
          {"Name": "Lemon", "Calories": "15"},
          {"Name": "Lime", "Calories": "20"},
          {"Name": "Nectarine", "Calories": "60"},
          {"Name": "Orange", "Calories": "80"},
          {"Name": "Peach", "Calories": "60"},
          {"Name": "Pear", "Calories": "100"},
          {"Name": "Pineapple", "Calories": "50"},
          {"Name": "Plums", "Calories": "70"},
          {"Name": "Strawberries", "Calories": "50"},
          {"Name": "Sweet", "Calories": "100"},
          {"Name": "Tangerine", "Calories": "50"},
          {"Name": "Watermelon", "Calories": "80"}]

for i in range(len(fruits)):
    if str(prompt).capitalize() == fruits[i]["Name"]:
      print("Calories:", fruits[i]["Calories"])
    else: pass
      



