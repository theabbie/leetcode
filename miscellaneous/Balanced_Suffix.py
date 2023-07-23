from collections import Counter

t = int(input())

apb = "abcdefghijklmnopqrstuvwxyz"

for _ in range(t):
    n, k = map(int, input().split())
    s = input()
    s = sorted(s)
    res = []
    for c in s:
        
    res.reverse()
    print("".join(res))