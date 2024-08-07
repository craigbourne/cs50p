# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.

prompt = input("What is the answer to the Great Question of Life, the Universe and Everything?\n")

if prompt.strip() == "42": print("yes")
elif prompt.lower().strip() == "forty two": print("yes")
elif prompt.lower().strip() == "forty-two": print("yes")
else: print("no")