def encode(s):
    n = len(s)
    res = []
    i = 0
    while i < n:
        ctr = 1
        while i < n - 1 and s[i] == s[i + 1]:
            ctr += 1
            i += 1
        if ctr == 1:
            ctr = ""
        res.append((s[i], ctr))
        i += 1
    return "".join(f"{r[0]}{r[1]}" for r in res)

def decode(s):
    n = len(s)
    lastchar = None
    ctr = 0
    res = []
    for i in range(n):
        if s[i].isalpha():
            lastchar = s[i]
            ctr = 0
        if s[i].isdigit():
            ctr = 10 * ctr + int(s[i])
        if i == n - 1 or s[i + 1].isalpha():
            if s[i].isalpha() and (i == n - 1 or s[i + 1].isalpha()):
                ctr = 1
            res.append((lastchar, ctr))
            ctr = 0
    return "".join(c * v for c, v in res)

s = "aabbbcdeeefaabcd"
encoded = encode(s)
decoded = decode(encoded)

print(f"s = {s}")
print(f"encoded = {encoded}")
print(f"decoded = {decoded}")
print(f"equal = {s == decoded}")