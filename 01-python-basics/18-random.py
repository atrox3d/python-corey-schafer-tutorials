#
#   https://www.youtube.com/watch?v=KzqSDvzOFNA
#
#   Python Tutorial: Generate Random Numbers and Data Using the random Module
#
#################################################################################
from modules import utils
import random

utils.banner("get float betweem 0 and 1 with .random")
for i in range(1, 10):
    print(random.random())

utils.banner("get float betweem two values with .uniform")
for i in range(1, 10):
    print(random.uniform(1, i))

utils.banner("get integer betweem two values with .randint")
for i in range(1, 10):
    print(random.randint(1, i))

utils.banner("get list item with .choice")
greetings = [
    "hello",
    "hi",
    "hey",
    "howdy",
    "hola"
]
for i in range(1, 10):
    print(random.choice(greetings))

utils.banner("get multiple list items with .choices")
colors = [
    'red',
    'black',
    'green',
]
for i in random.choices(colors, weights=[18, 18, 2], k=10):
    print(i)

utils.banner('shuffle a list with .shuffle')
cards = list(range(1, 53))
print(cards)
print("shuffling...")
random.shuffle(cards)
print(cards)

utils.banner('get a list of unique elements with .sample')
hand = random.sample(cards, k=5)
print(hand)


