num = [7, 5, 7, 8]
p = 129
curr = 0
base = 10 % p

for n in num:
    curr = (curr * base + n) % p

print(curr)