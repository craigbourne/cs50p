import random

# ========== choice ==========
# coin_toss = random.choice(["heads", "tails"])
# print(coin_toss)

# ========== random integer ==========
# random_number = random.randint(1,10)
# print(random_number)

# ========== shuffle ==========
suits = ["hearts", "diamonds", "clubs", "spades"]
shuffle_suits = random.shuffle(suits)
for suit in suits:
  print(suit)