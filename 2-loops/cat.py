# ========== while loops ==========
"""

i = 0
while i < 3:
  print("ho")
  i += 1

"""

# ========== for loops ==========
"""
sounds = ["meow", "woof", "hoot", "moo"]

# method 1
for i in range(4):
  print(sounds[i])

# method 2
for sound in sounds:
  print(sound)

# method 3
print("meow\n" *3, end="")

# method 4
while True:
  n = int(input("What's n? "))
  if n > 0:
    break

for _ in range(n):
  print("meow")

"""

# with a main() function

def main():
  count = get_count()
  meow(count)

def get_count():
  while True:
    n = int(input("How many meow's? "))
    if n > 0:
      return n

def meow(n):
  for _ in range(n):
    print("meow")

if __name__ == "__main__":
  main()