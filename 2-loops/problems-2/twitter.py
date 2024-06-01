"""
Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

vowels = ["a","e","i","o","u"]

prompt = input("Input: ")
new_string = ""
for letter in prompt:
  if letter.lower() not in vowels:
      new_string += letter
print(new_string)
