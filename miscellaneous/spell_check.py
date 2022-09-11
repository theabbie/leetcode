from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    if Counter(s) == Counter("Timur"):
        print("YES")
    else:
        print("NO")