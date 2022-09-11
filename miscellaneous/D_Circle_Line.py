n = int(input())

dist = list(map(int, input().split()))

s, t = map(int, input().split())

s, t = min(s, t), max(s, t)

p = [0]

for el in dist:
    p.append(p[-1] + el)

c = p[t - 1] - p[s - 1]

print(min(c, p[-1] - c))