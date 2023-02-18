from collections import Counter

t = int(input())

def valid(arr, n):
    return sorted(arr) == list(range(1, n + 1))

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ctr = Counter(arr)
    k = max(ctr.values())
    if k > 2:
        print("NO")
    elif k == 1:
        print("YES")
        print(*arr)
        print(*arr)
    else:
        a = []
        b = []
        singles = set()
        doubles = []
        mp = {}
        for el in arr:
            if ctr[el] == 1:
                singles.add(el)
            if ctr[el] == 2:
                doubles.append(el)
        unused = []
        for i in range(1, n + 1):
            if i not in singles:
                unused.append(i)
        doubles.sort()
        for el in doubles:
            mp[el] = unused.pop(0)
        seendouble = set()
        for el in arr:
            if ctr[el] == 1:
                a.append(el)
                b.append(el)
            else:
                if el in seendouble:
                    a.append(mp[el])
                    b.append(el)
                else:
                    seendouble.add(el)
                    a.append(el)
                    b.append(mp[el])
        if valid(a, n) and valid(b, n) and arr == [max(a[i], b[i]) for i in range(n)]:
            print("YES")
            print(*a)
            print(*b)
        else:
            print("NO")