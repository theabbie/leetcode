t = int(input())

def solve(s):
    x = "FBFFBFFB"
    if s in (x + x + x):
        return "YES"
    else:
        return "NO"

for _ in range(t):
    k = int(input())
    s = input()
    print(solve(s))