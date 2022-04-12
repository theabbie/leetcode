import bisect

t = int(input())

ranges = []

minval = float('inf')
maxval = float('-inf')

for _ in range(t):
    a, b = [int(x) for x in input().split()]
    ranges.append((a, b))
    
interesting = []

for i in range(minval, maxval + 1):
    n = i
    p = 1
    s = 0
    while n > 0:
        d = n % 10
        n = n // 10
        p *= d
        s += d
    if p % s == 0:
        interesting.append(i)
    
for a, b in ranges:
    ctr = bisect.bisect_right(interesting, b) - bisect.bisect_left(interesting, a)
    print("Case #{}: {}".format(_ + 1, ctr))
