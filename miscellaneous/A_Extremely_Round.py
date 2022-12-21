t = int(input())

def count(x):
    if x < 10:
        return x
    if x < 100:
        return x // 10 + count(9)
    if x < 1000:
        return x // 100 + count(99)
    if x < 10000:
        return x // 1000 + count(999)
    if x < 100000:
        return x // 10000 + count(9999)
    if x < 1000000:
        return x // 100000 + count(99999)

for _ in range(t):
    n = int(input())
    print(count(n))