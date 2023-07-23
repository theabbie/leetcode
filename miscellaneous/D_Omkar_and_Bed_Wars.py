from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    attack = defaultdict(set)
    attacked = defaultdict(set)
    for i in range(n):
        l = (n + i - 1) % n
        r = (i + 1) % n
        if s[i] == "L":
            attacked[l].add(i)
        else:
            attacked[r].add(i)
    print(attacked)