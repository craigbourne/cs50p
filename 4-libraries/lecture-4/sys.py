import sys

# print(f"Hello, my name is {sys.argv[1]} and the name of this file is {sys.argv[0]}!")

# try:
#   print(f"Hello, my name is {sys.argv[1]} and the name of this file is {sys.argv[0]}!")
# except IndexError: 
#   print(f"The name of this file is {sys.argv[0]}!")


# check for errors
if len(sys.argv) < 2:
  sys.exit("Too few arguments")

# for arg in sys.argv:
#   if arg != "name.py":
#     print(f"hello my name is {arg}")

for arg in sys.argv[1:len(sys.argv)]: # can also do sys.argv[1:] with no 2nd value after colon
  print(f"Hello my name is {arg}")

