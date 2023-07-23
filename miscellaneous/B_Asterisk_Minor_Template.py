t = int(input())

def solve(a, b):
    i = 0
    while i < len(a) and i < len(b) and a[i] == b[i]:
        i += 1
    if i >= 1:
        print("YES")
        print(a[:i] + ("*" if i < max(len(a), len(b)) else ""))
        return
    i = 0
    while i < len(a) and i < len(b) and a[len(a) - i - 1] == b[len(b) - i - 1]:
        i += 1
    if i >= 1:
        print("YES")
        print("*" + a[-i:])
        return
    seen = set()
    for i in range(len(a) - 1):
        seen.add(a[i:i+2])
    for i in range(len(b) - 1):
        if b[i:i+2] in seen:
            print("YES")
            print("*" + b[i:i+2] + "*")
            return
    print("NO")

for _ in range(t):
    a = input()
    b = input()
    solve(a, b)