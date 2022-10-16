t = int(input())

for tt in range(1, t + 1):
    rs, rh = map(int, input().split())
    red = []
    yellow = []
    redmin = float('inf')
    yellowmin = float('inf')
    n = int(input())
    for __ in range(n):
        x, y = map(int, input().split())
        if x * x + y * y <= (rs + rh) * (rs + rh):
            redmin = min(redmin, x * x + y * y)
            red.append(x * x + y * y)
    m = int(input())
    for __ in range(m):
        x, y = map(int, input().split())
        if x * x + y * y <= rs * rs + rh * rh:
            yellowmin = min(yellowmin, x * x + y * y)
            yellow.append(x * x + y * y)
    rscore = 0
    yscore = 0
    for r in red:
        if r < yellowmin:
            rscore += 1
    for y in yellow:
        if y < redmin:
            yscore += 1
    print(f"Case #{tt}: {rscore} {yscore}")