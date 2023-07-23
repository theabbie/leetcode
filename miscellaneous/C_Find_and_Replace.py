t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    assigned = {}
    res = []
    for i in range(n):
        if s[i] not in assigned:
            assigned[s[i]] = i % 2
        res.append(assigned[s[i]])
    valid = True
    for i in range(n):
        if res[i] != i % 2:
            valid = False
            break
    print("YES" if valid else "NO")