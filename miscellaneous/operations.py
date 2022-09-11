t = int(input())

for _ in range(t):
    b, c = map(int, input().split())
    if (b + c) % 2 == 0:
        if b == c:
            if b != 0:
                print(1)
            else:
                print(0)
        else:
            print(2)
    else:
        print(-1)