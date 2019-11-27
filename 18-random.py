#
#   https://www.youtube.com/watch?v=KzqSDvzOFNA
#
#################################################################################
import utils
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

