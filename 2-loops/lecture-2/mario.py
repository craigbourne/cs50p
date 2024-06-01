def main():
  column(3)
  row(4)
  wall(6,4)

def column(height):
  print(" ")
  for _ in range(height):
    print("#")

def row(width):
  print(" ")
  print("?" * width)

def wall(width, height):
  print(" ")
  for _ in range(height):
    print("X" * width)

main()