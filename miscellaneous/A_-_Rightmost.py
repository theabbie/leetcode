s = input()

n = len(s)

res = -1

for i in range(n):
    if s[i] == 'a':
        res  = i + 1

print(res)