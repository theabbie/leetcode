n, m = map(int, input().split())

a = input().split()

b = input().split()

p = list(map(int, input().split()))

mp = {}

for i in range(m):
    mp[b[i]] = p[i + 1]

res = 0

for el in a:
    res += mp.get(el, p[0])

print(res)