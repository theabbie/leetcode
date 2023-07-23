from collections import Counter

t = int(input())

mp = {"A": ["A", "AB"], "B": ["B", "AB"], "AB": ["AB"], "O": ["A", "B", "AB"]}

for _ in range(t):
    n = int(input())
    ctr = Counter(input().split())
    res = max(ctr["O"] + ctr["A"] + ctr["AB"], ctr["O"] + ctr["B"] + ctr["AB"])
    print(res)