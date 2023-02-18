import random

t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def check(arr, x):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(arr[i] + x, arr[j] + x) != 1:
                return False
    return True

def solve(arr):
    for _ in range(100):
        x = random.randint(1, 10 ** 18)
        if check(arr, x):
            return True
    return False

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print("YES" if solve(arr) else "NO")