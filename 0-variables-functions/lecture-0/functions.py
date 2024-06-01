#collecting name and calling hello() with name passed in
def main():
  name = input("What is your name? ")
  hello(name)

# print hello to value stored in name which is passed to to
def hello(to="world"):
  print(f"Hello, {to}")

hello()
main() 
