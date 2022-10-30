t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = input()
    mp = {}
    for i in range(n):
        mp[arr[i]] = s[i]
    if s == "".join(mp[el] for el in arr):
        print("YES")
    else:
        print("NO")