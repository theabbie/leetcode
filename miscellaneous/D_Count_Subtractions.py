a, b = map(int, input().split())

res = 0

while a != b:
    if a == 0 or b == 0:
        res -= 1
        break
    if a < b:
        res += b // a
        b = b % a
    elif a > b:
        res += a // b
        a = a % b

print(res)