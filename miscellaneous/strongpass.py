t = int(input())

for tt in range(1, 1 + t):
    n = int(input())
    res = input()
    spc = "#@*&"
    sp = 0
    upc = 0
    lc = 0
    dg = 0
    for c in res:
        if c.isupper():
            upc += 1
        elif c.islower():
            lc += 1
        elif c in spc:
            sp += 1
        else:
            dg += 1
    if upc == 0:
        res += "A"
    if lc == 0:
        res += "a"
    if dg == 0:
        res += "0"
    if sp == 0:
        res += spc[0]
    while len(res) < 7:
        res += "a"
            
    print(f"Case #{tt}: {res}")
