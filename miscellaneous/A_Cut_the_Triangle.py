t = int(input())

for _ in range(t):
    points = []
    input()
    points.append(tuple(map(int, input().split())))
    points.append(tuple(map(int, input().split())))
    points.append(tuple(map(int, input().split())))
    x = set()
    y = set()
    for i, j in points:
        x.add(i)
        y.add(j)
    print("YES" if len(x) == 3 or len(y) == 3 else "NO")