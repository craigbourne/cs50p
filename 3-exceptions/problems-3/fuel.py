'''
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
'''

def main():
  result = calc_fuel()
  print(result)

def get_perc():
# prompts the user for a fraction formatted as X/Y
  while True:
    try:
      prompt = input("Fraction: ").split("/")
      fraction = int(prompt[0]) / int(prompt[1])
      perc = int(round(fraction * 100))
      if fraction > 1:
        print("Fraction cannot be greater than 1.")
        continue
    except (ValueError, ZeroDivisionError):
      print("That is not a fraction")
    else:
      return perc

def calc_fuel():
  perc = get_perc()
  result = ""
  # if 99% or more remains, output F instead to indicate that the tank is essentially full
  if perc >= 99:
    result = "F"
  # If, though, 1% or less remains, output E
  elif perc <= 1:
    result = "E"
  # outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank
  else: result = f"{perc}%"
  return result

main()
