t = int(input())

def getsmaller(arr):
    n = len(arr)
    s = []
    smaller = [n] * n
    s.append(0)
    for i in range(1, n):
        if len(s) == 0:
            s.append(i)
            continue
        while len(s) != 0 and arr[s[-1]] > arr[i]:
            smaller[s[-1]] = i
            s.pop()
        s.append(i)
    while len(s) != 0:
        smaller[s[-1]] = n
        s.pop()
    return smaller

for tt in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    p = [0]
    for el in arr:
        p.append(p[-1] + el)
    smaller = getsmaller(p)
    freq = [0] * n
    res = 0
    for i in range(n + 1):
        j = smaller[i]
        if j - 2 >= i:
            print(i, j - 2)
            freq[i] += j - i - 1
            if i + 1 < n:
                freq[i + 1] += i - j
    print(freq)
    for i in range(1, n):
        freq[i] += freq[i - 1]
    for i in range(1, n):
        freq[i] += freq[i - 1]
    print(freq)
    for i in range(n):
        res += freq[i] * arr[i]
    print(f"Case #{tt}: {res}")