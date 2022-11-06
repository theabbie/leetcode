s = input()

n = len(s)

ss = s + s

print(min(ss[i:i+n] for i in range(n)))