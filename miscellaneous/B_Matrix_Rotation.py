t = int(input())

def isgood(a, b, c, d):
    return a <= b and a <= c and b <= d and c <= d

for _ in range(t):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print("YES" if isgood(a, b, c, d) or isgood(c, a, d, b) or isgood(d, c, b, a) or isgood(b, d, a, c) else "NO")