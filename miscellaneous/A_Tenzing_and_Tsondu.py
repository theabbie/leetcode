t = int(input())

for _ in range(t):
    m, n = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    if sum(a) > sum(b):
        print("Tsondu")
    elif sum(a) < sum(b):
        print("Tenzing")
    else:
        print("Draw")