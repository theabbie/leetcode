t = int(input())

for _ in range(t):
    a = input()
    b = input()
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(a):
        print("Case #{}: {}".format(_ + 1, len(b) - len(a)))
    else:
        print("Case #{}: {}".format(_ + 1, "IMPOSSIBLE")
