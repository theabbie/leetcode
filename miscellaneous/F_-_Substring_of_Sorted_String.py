class FenwickTree:
    def __init__(self, x):
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

n = int(input())

s = list(input())

q = int(input())

res = []

valids = []

for i in range(n):
    valids.append(1 if ((i == 0 or s[i - 1] <= s[i]) and (i == n - 1 or s[i] <= s[i + 1])) else 0)

fw = FenwickTree(valids)

chars = [FenwickTree([0] * n) for _ in range(26)]

for i in range(n):
    chars[ord(s[i]) - ord('a')].update(i, 1)

for _ in range(q):
    curr = input().split()
    if curr[0] == "1":
        i = int(curr[1]) - 1
        c = curr[2]
        prev = fw.query(i + 1) - fw.query(i)
        s[i] = c
        newval = 1 if ((i == 0 or s[i - 1] <= s[i]) and (i == n - 1 or s[i] <= s[i + 1])) else 0
        fw.update(i, newval - prev)
        i -= 1
        if 0 <= i < n:
            prev = fw.query(i + 1) - fw.query(i)
            newval = 1 if ((i == 0 or s[i - 1] <= s[i]) and (i == n - 1 or s[i] <= s[i + 1])) else 0
            fw.update(i, newval - prev)
        i += 2
        if 0 <= i < n:
            prev = fw.query(i + 1) - fw.query(i)
            newval = 1 if ((i == 0 or s[i - 1] <= s[i]) and (i == n - 1 or s[i] <= s[i + 1])) else 0
            fw.update(i, newval - prev)
    else:
        l, r = int(curr[1]), int(curr[2])
        l -= 1
        r -= 1
        valid = True
        minchar = maxchar = None
        for x in range(26):
            if chars[x].query(r + 1) - chars[x].query(l) > 0:
                if minchar == None:
                    minchar = x
                maxchar = x
        for x in range(26):
            if minchar < x < maxchar:
                if chars[x].query(r + 1) - chars[x].query(l) < chars[x].query(n):
                    valid = False
                    break
        print("Yes" if valid and (fw.query(r + 1) - fw.query(l) == r - l + 1) else "No")

print("\n".join(res))