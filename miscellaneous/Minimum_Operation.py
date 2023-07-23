t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = 1 + 10 ** 6

sp = [1] * N
v = [False] * N

for i in range(2, N, 2):
    sp[i] = 2

for i in range(3, N, 2):
    if not v[i]:
        sp[i] = i
        j = i
        while j * i < N:
            v[j * i] = True
            sp[j * i] = i
            j += 2

plist = set()

for i in range(2, N):
    if sp[i] == i:
        plist.add(i)

for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    if len(set(arr)) == 1:
        print(0)
        continue
    g = arr[0]
    for el in arr:
        g = gcd(g, el)
    if g > 1:
        print(1)
        print(g)
    else:
        print(1)
        curr = set()
        for el in arr:
            while el > 1:
                curr.add(sp[el])
                el //= sp[el]
        res = max(arr)
        for el in plist:
            if el <= m and el not in curr:
                res = el
                break
        print(res)