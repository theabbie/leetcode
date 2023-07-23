n = int(input())

s = input()

def check(s, n):
    x, y = 0, 0
    v = {(0, 0)}
    for c in s:
        if c == "R":
            y += 1
        if c == "L":
            y -= 1
        if c == "U":
            x -= 1
        if c == "D":
            x += 1
        if (x, y) in v:
            return "Yes"
        v.add((x, y))
    return "No"

print(check(s, n))