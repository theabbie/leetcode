n, a, b = map(int, input().split())

arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] == a + b:
        print(i + 1)
        break