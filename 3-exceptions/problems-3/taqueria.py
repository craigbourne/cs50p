'''
In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
'''

items = {
  "Baja Taco": 4.25,
  "Burrito": 7.50,
  "Bowl": 8.50,
  "Nachos": 11.00,
  "Quesadilla": 8.50,
  "Super Burrito": 8.50,
  "Super Quesadilla": 9.50,
  "Taco": 3.00,
  "Tortilla Salad": 8.00
}

# enable a user to place an order, prompting them for items, one per line
total = 0
while total >= 0:
  try:
    prompt = input("Item: ").title()
    total += float(items[prompt])
#  check for items not on the menu or not of the right type
  except (KeyError, ValueError):
    print("That is not on the menu")
  except(EOFError):
    break
# After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to two decimal places.
  else:
    print(f"Total: ${total:.2f}")
