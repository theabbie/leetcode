n = int(input())

d = set()

valid = True

for _ in range(n):
    s = input()
    if s[0] not in "HDCS":
        valid = False
    if s[1] not in "A23456789TJQK":
        valid = False
    d.add(s)

if len(d) < n:
    valid = False

print("Yes" if valid else "No")