# Asks user or a name, remove prevailing and trailing whitespace and capitalize
name = input("What is your full name? ").strip().title()
first_name, last_name = name.split(" ")

# Says hello to the user in the terminal
# print("Hello, " + name)
# print("Hello, ", name) # This produces a double space. Passing two arguments adds a space
print(f"Hello, {first_name}") 




"""
This is a 
multiline comment 
I think

"""