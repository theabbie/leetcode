t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    c = s[n // 2]
    i = None
    j = None
    if n & 1:
        i = n // 2
        j = n // 2
    else:
        i = n // 2 - 1
        j = n // 2
    while 0 <= i <= j < n and s[i] == s[j] == c:
        i -= 1
        j += 1
    print(j - i - 1)