"""
x = int(input("What's x? "))
print(f"x is {x}")

If user enters a string "hello" rather than an int above, it produces:

=> ValueError: invalid literal for int() with base 10: 'hello'

A ValueError is caused when a function (like int()) receives an argument of the correct type but an inappropriate value.
"""

# ========================= try & except =========================

"""
try:
  x = int(input("What's x? "))
  print(f"x is {x}")
except ValueError:
  print("x is not an integer")
"""

# ========================= NameError =========================
# A better way to do the above is to try to only use lines that could produce errors in the try/except. So, it is best to move the print statement out:

"""
try:
  x = int(input("What's x? "))
except ValueError:
  print("x is not an integer")

print(f"x is {x}")
"""

# This produces => NameError: name 'x' is not defined if a non-int value is entered into the int(). A 'NameError: name 'x' is not defined error' is raised when the program attempts to access or use a variable that has not been defined or assigned a value. x is not storing non-int values and it will create an ValueError if a non-int is entered. Therefore the value will not be assigned to 'x'. The print will run nomatter what but cannot print a variable value that doesn't exist, creating a NameError. So we can use the else keyword, which only executes if we have tried and succeeded:

"""
try:
  x = int(input("What's x? "))
except ValueError:
  print("x is not an integer")
else:
  print(f"x is {x}")
"""

# ========== We can improve by adding a loop ==========
"""
while True:
  try:
    x = int(input("What's x? ")) #try to get input and convert to int
    # break can also go here rather than in
  except:
    print("x is not an integer") # if there's a ValueError, print and reprompt
  else:
    break # if x is int break out of loop and print below outside of loop can execute
print(f"x is {x}")
"""

# ========== Move everything to functions, clean up and use pass ==========
def main():
  x = get_int("What's x? ")
  print(f"x is {x}")
  
def get_int(prompt):
  while True:
    try: return int(input(prompt)) 
    except ValueError: pass

if __name__ == "__main__": main()
