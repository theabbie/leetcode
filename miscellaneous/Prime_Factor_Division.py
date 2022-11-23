t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def factors(a, b):
    c = 2
    while b > 1:
        if b % c == 0:
            b = b // c
            if a % c != 0:
                return False
        else:
            c += 1
    return True

for _ in range(t):
    a, b = map(int, input().split())
    g  = gcd(a, b)
    b = b // g
    a = gcd(a, b)
    if factors(a, b):
        print("YES")
    else:
        print("NO")