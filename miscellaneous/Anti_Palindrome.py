t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    ctr = [0] * 26
    for c in s:
        ctr[ord(c) - ord('a')] += 1
    res = float('inf')
    e = o = 0
    for c in range(26):
        if ctr[c] & 1:
            o += 1
        elif ctr[c] > 0:
            e += 1
    if o > 1:
        print(0)
    elif o == 0:
        print(1)
    else:
        print(2 if e == 0 else 1)