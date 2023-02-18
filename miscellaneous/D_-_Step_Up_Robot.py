from collections import defaultdict

n = int(input())

a = list(map(int, input().split()))

m = int(input())

b = list(map(int, input().split()))

x = int(input())

possible = [-1] * (x + 1)

possible[x] = True

for bi in b:
    if bi <= x:
        possible[bi] = False

for i in range(x, -1, -1):
    if possible[i] == -1:
        for ai in a:
            if i + ai <= x and possible[i + ai]:
                possible[i] = True
                break
        if possible[i] == -1:
            possible[i] = False

print("Yes" if possible[0] == True else "No")