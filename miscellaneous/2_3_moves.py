t = int(input())

for _ in range(t):
    n = int(input())
    minmoves = float('inf')
    for x in range(n + 3):
        if abs(n - 3 * x) % 2 == 0:
            minmoves = min(minmoves, x + abs(n - 3 * x) // 2)
    print(minmoves)