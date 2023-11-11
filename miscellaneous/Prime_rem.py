def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

arr = list(map(int, input().split()))

q = min(arr)

arr.remove(q)

lcm = arr[0]

for el in arr:
    lcm = lcm * el // gcd(lcm, el)
    
i = 2

prime = True

while i * i <= q + lcm:
    if (q + lcm) % i == 0:
        prime = False
        break
    i += 1

print(q + lcm if prime else None)