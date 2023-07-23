import random

N = 10 ** 5

for _ in range(3):
    print(random.choices(range(1, 100), k = N))