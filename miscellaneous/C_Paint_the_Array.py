t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    vals = [0, 0]
    for i in range(n):
        vals[i % 2] = gcd(vals[i % 2], abs(arr[i]))
    res = 0
    for el in vals:
        if el == 0:
            continue
        for b in range(2):
            valid = True
            for i in range(n):
                if i % 2 == b and arr[i] % el != 0:
                    valid = False
                    break
                if i % 2 != b and arr[i] % el == 0:
                    valid = False
                    break
            if valid:
                res = el
                break
    print(res)