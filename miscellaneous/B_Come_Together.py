t = int(input())

def count(a, b):
    if a == 0 or b == 0:
        return 0    
    if (a < 0) != (b < 0):
        return 0
    return min(abs(a), abs(b))

for _ in range(t):
    ax, ay = map(int, input().split())
    bx, by = map(int, input().split())
    cx, cy = map(int, input().split())
    print(count(bx - ax, cx - ax) + count(by - ay, cy - ay) + 1)