t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    odds = []
    evens = []
    for el in arr:
        if el & 1:
            odds.append(el)
        else:
            evens.append(el)
    odds.sort(reverse = True)
    evens.sort(reverse = True)
    for i in range(n):
        if arr[i] & 1:
            arr[i] = odds.pop()
        else:
            arr[i] = evens.pop()
    print("YES" if arr == sorted(arr) else "NO")