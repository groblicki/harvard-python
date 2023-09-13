# from random import choice
import random
import statistics


coin = random.choice(["heads", "tiles"])
print(coin)

number = random.randint(0, 100)
print(number)

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)

print(statistics.mean([random.randint(0, 100), random.randint(0, 100)]))
