t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())
    if c % 2 == 0:
        print("First" if a > b else "Second")
    else:
        print("First" if a + 1 > b else "Second")