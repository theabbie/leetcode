t = int(input())

def solve(s, n):
    k = n // 2
    a = s[:k][::-1]
    b = s[n-k:n]
    i = 0
    while i < k and a[i] == b[i]:
        i += 1
    j = k - 1
    while j >= 0 and a[j] == b[j]:
        j -= 1
    for x in range(i, j + 1):
        if a[x] == b[x]:
            return "No"
    return "Yes"

for _ in range(t):
    n = int(input())
    s = input()
    print(solve(s, n))