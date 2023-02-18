n = int(input())

s = []

for _ in range(n):
    s.append(input())

print("\n".join(s[::-1]))