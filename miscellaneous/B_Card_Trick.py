t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    shuffles = map(int, input().split())
    print(arr[sum(shuffles) % n])