"""
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination.
"""

# initial amount to pay
amount_due = 50

# insert coin while some amount is due
while amount_due > 0:
  print(f"Amount due: {amount_due}")
  inserted = int(input("Insert coins: "))
  # check if coin is accepted & if so, deduct from amount due. Otherwise (19), say coin not accepted
  if inserted == 5 or inserted == 10 or inserted == 25:
    amount_due -= inserted
    # after coin inserted, check if there is outstanding amount due or change to give
    if amount_due < 0:
      print(f"Change owed: {abs(amount_due)}")
  else: 
    print(f"Not accepted. Amount due: {amount_due}")
