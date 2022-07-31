t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ctr = 0
    for c in s:
        if c == ')':
            ctr += 1
        else:
            ctr = 0
    if ctr > n - ctr:
        print("Yes")
    else:
        print("No")