n = int(input())

s = input()

res = []

for i in range(1, n):
    j = 0
    while j < n - i and s[j] != s[j + i]:
        j += 1
    res.append(j)

print("\n".join(map(str, res)))