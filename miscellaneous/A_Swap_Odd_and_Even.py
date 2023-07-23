s = list(input())

n = len(s)

for i in range(n // 2):
    s[2 * i], s[2 * i + 1] = s[2 * i + 1], s[2 * i]

print("".join(s))