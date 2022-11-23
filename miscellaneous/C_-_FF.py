n, q = map(int, input().split())

valid = set()

for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        valid.add((a, b))
    if t == 2:
        if (a, b) in valid:
            valid.remove((a, b))
    if t == 3:
        print("Yes" if ((a, b) in valid and (b, a) in valid) else "No")