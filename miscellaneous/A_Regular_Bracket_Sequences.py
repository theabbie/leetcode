t = int(input())

for _ in range(t):
    n = int(input())
    for k in range(n):
        print("(" * k + "()" * (n - k) + ")" * k)