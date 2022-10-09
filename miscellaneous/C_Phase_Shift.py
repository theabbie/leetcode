t = int(input())

val = lambda c: ord(c) - ord('a')
gch = lambda i: chr(ord('a') + i)
inc = lambda c, shift: chr(ord('a') + (ord(c) - ord('a') + shift) % 26)
dec = lambda c: chr(ord('a') + (26 + ord(c) - ord('a') - 1) % 26)

for _ in range(t):
    n = int(input())
    s = list(input())
    cmap = {}
    revcmap = {}
    for i in range(n):
        if s[i] not in cmap:
            j = val(s[i])
            found = False
            for x in range(val(max(list(revcmap.keys()) + ["a"])), j):
                if gch(x) not in revcmap:
                    cmap[s[i]] = gch(x)
                    revcmap[gch(x)] = s[i]
                    found = True
                    break
            if not found:
                shift = 1
                while cmap.get(s[i], -1) == inc(s[i], shift) or cmap.get(inc(s[i], shift), -1) == s[i]:
                    shift += 1
                cmap[s[i]] = inc(s[i], shift)
                revcmap[inc(s[i], shift)] = s[i]
        s[i] = cmap[s[i]]
    print("".join(s))