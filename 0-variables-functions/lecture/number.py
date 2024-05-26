# x = float(input("what is your first number? "))
# y = float(input("what is your second number? "))

# add = x + y
# subtract = x - y
# divide = x * y
# multiply = x / y

# formatting for commas in numbers
# add_commas = f"{add:,}"
# print(add_commas)

#  To two decimal places 
# print(f"{multiply:.2f}")

def main():
  x = int(input("What's the value of x? ")) # assigns input to variable
  square(x) # calls the square function and passes in x value
  print(f"x squared is {square(x)}")

def square(num):
  return num ** 2

main()