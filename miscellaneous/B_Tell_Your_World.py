from collections import Counter

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def slope(a, b):
    mul = gcd(abs(a), abs(b))
    if mul != 0:
        a, b = a // mul, b // mul
    if b < 0:
        a *= -1
        b *= -1
    return (a, b)

n = int(input())

arr = list(map(int, input().split()))

valid = set()

for i in range(1, n + 1):
    valid.add(i * (i - 1) // 2)

pos = False

for i in range(1, n):
    m = slope(arr[i] - arr[0], i)
    diffs = set()
    diffslope = -1
    for j in range(1, n):
        curr = slope(arr[j] - arr[0], j)
        if curr != m:
            diffslope = j
            break
    if diffslope != -1:
        for j in range(1, n):
            if j == diffslope:
                continue
            curr = slope(arr[j] - arr[0], j)
            if curr != m:
                diffs.add(slope(arr[j] - arr[diffslope], j - diffslope))
    else:
        break
    if len(diffs) == 0 or (len(diffs) == 1 and m in diffs):
        pos = True
        break

slopes = set()

for i in range(2, n):
    slopes.add(slope(arr[i] - arr[1], i - 1))

if slope(arr[1] - arr[0], 1) in slopes:
    slopes.remove(slope(arr[1] - arr[0], 1))

if len(slopes) == 1:
    pos = True

print("Yes" if pos else "No")