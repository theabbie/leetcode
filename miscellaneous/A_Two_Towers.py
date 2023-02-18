t = int(input())

def valid(a):
    n = len(a)
    for i in range(n - 1):
        if a[i] == a[i + 1]:
            return False
    return True

def check(a, b):
    while len(a) > 1:
        b.append(a.pop())
    if valid(b):
        return "YES"
    while len(b) > 1:
        a.append(b.pop())
        if valid(a) and valid(b):
            return "YES"
    return "NO"

for _ in range(t):
    m, n = map(int, input().split())
    a = list(input())
    b = list(input())
    print(check(a, b))