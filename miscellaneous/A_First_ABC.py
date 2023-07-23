n = int(input())

s = input()

res = 0

aa = bb = cc = 0

for c in s:
    res += 1
    if c == "A":
        aa = 1
    if c == "B":
        bb = 1
    if c == "C":
        cc = 1
    if aa + bb + cc == 3:
        break

print(res)