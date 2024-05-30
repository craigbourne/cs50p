# implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.

def main():
  camel()

def camel():
  snake_case = ""
  camel_case = input("camelCase: ")
  for letter in camel_case:
    if letter.isupper():
      snake_case += f"_{letter.lower()}"
    else:
      snake_case += letter
  print(snake_case)



if __name__ == "__main__":
  main()