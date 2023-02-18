M = 10 ** 9 + 7

t = int(input())

def smallest(arr, i, n, tight):
    return

for _ in range(t):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    curr = 0
    for el in arr:
        curr = (b * curr + el) % M
    print((smallest(arr, 0, n, True) - curr))