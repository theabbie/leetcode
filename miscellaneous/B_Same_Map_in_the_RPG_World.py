m, n = map(int, input().split())

def equal(a, b, s, t, m, n):
    for i in range(m):
        for j in range(n):
            if a[(i + s) % m][(j + t) % n] != b[i][j]:
                return False
    return True

def check(a, b, m, n):
    for s in range(m):
        for t in range(n):
            if equal(a, b, s, t, m, n):
                return "Yes"
    return "No"

a = []
b = []

for _ in range(m):
    a.append(input())

for _ in range(m):
    b.append(input())

print(check(a, b, m, n))