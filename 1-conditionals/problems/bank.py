# Implement a program that prompts the user for a greeting
# Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively
greeting = input("Greeting: ").lower().strip()
# If the greeting starts with “hello”, output $0
if greeting.startswith("hello"):
  print("$0")
# If the greeting starts with an “h” (but not “hello”), output $20
elif greeting.startswith("h") and greeting.lower() != "hello":
  print("$20")
  # Otherwise, output $100
else:
  print("$100")