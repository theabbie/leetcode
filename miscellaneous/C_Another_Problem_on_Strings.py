k = int(input())

s = input()

n = len(s)

back = {}

front = {}

prev = None

for i in range(n):
    if prev != None:
        back[i] = i - prev - 1
    else:
        back[i] = 0
    if s[i] == "1":
        prev = i

prev = None

for i in range(n - 1, -1, -1):
    if prev != None:
        front[i] = prev - i
    else:
        front[i] = 0
    if s[i] == "1":
        prev = i

print(back, front)

c = 0

i = 0

res = 0

for j in range(n):
    c += int(s[j])
    while i <= j and c > k:
        c -= int(s[i])
        i += 1
    if c == k:
        res += 1 + back[i] + front[i]

print(res)