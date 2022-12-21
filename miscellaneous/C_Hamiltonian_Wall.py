t = int(input())

def check(wall, n, i, j):
    seen = False
    while j < n:
        if wall[i][j] != "B":
            return False
        if seen:
            j += 1
            seen = False
        elif wall[1 - i][j] == "B":
            i = 1 - i
            seen = True
        else:
            j += 1
            seen = False
    return True

for _ in range(t):
    n = int(input())
    wall = []
    wall.append(input())
    wall.append(input())
    print("YES" if check(wall, n, 0, 0) or check(wall, n, 1, 0) else "NO")