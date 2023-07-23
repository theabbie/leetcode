t = int(input())

for _ in range(t):
    a, b = input().split()
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    if len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b
    n = len(a)
    res = a
    for i in range(10):
        for j in range(i, 10):
            pos = True
            for k in range(n):
                
            if pos:
                pass
    print(res)