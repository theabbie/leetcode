t = int(input())

def possible(a, b, c, carry):
    if a + b + c == 0:
        return carry == 0
    ax = a % 2
    bx = b % 2
    cx = c % 2
    if (ax + bx + carry) % 2 == cx:
        if possible(a >> 1, b >> 1, c >> 1, (ax + bx + carry) // 2):
            return True
    if (1 - ax + 1 - bx + carry) % 2 == 1 - cx:
        if possible(a >> 1, b >> 1, c >> 1, (1 - ax + 1 - bx + carry) // 2):
            return True
    return False

for _ in range(t):
    a, b, c = map(int, input().split())
    print("YES" if possible(a, b, c, 0) else "NO")