from collections import defaultdict

n, p = map(int, input().split())

probs = defaultdict(lambda: 1)

def prob(stamina, x, p, stop):
    probs[stamina] *= x
    if stop:
        return True
    if stamina <= 2:
        stop = True
    prob(stamina - 1, 1 - p / 100, p, stop)
    prob(stamina - 2, p / 100, p, stop)

prob(n, 1, p, False)

print(probs)