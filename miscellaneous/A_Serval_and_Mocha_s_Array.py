t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(arr[i], arr[j]) <= 2:
                return "Yes"
    return "No"

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr, n))