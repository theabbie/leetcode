a, b = map(int, input().split())

res = a // b

if a % b != 0:
    res += 1

print(res)