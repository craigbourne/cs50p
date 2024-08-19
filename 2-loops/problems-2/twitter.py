"""
Implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

prompt = input("Input: ")
no_vowels = ''
for letter in prompt:
  if letter.lower() not in ['a','e','i','o','u']:
    no_vowels += letter
print(no_vowels)