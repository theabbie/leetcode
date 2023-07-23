from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    found = False
    for M in [arr[-1], arr[1] * arr[-2]]:
        i = 1
        factors = set()
        while i * i <= M:
            if M % i == 0:
                factors.add(i)
                factors.add(M // i)
            i += 1
        if sorted(factors) == arr:
            print(M)
            found = True
            break
    if not found:
        print("laddu")