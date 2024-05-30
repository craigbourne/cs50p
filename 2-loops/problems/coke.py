"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

def main():
  pay()

def pay():
  coke = 50
  # insert coin while cost of coke is outstanding
  while coke > 0:
    inserted = int(input("Insert coins: "))
    # check if coin is accepted
    if inserted == 5 or inserted == 10 or inserted == 25:
      coke -= inserted
      if coke > 0:
        print(f"Amount due: {coke}")
      else:
        print(f"Change owed: {abs(coke)}")
    else: 
      print(f"Not accepted. Amount due: {coke}")

if __name__ == "__main__":
  main()