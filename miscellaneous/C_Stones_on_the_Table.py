n = int(input())
s = input()
res = 0
i = 0
while i < n:
    ctr = 1
    while i < n - 1 and s[i] == s[i + 1]:
        i += 1
        ctr += 1
    i += 1
    res += ctr - 1
print(res)