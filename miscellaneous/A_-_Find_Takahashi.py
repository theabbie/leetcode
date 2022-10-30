n = int(input())

arr = list(map(int, input().split()))

print(1 + max(range(n), key = lambda i: arr[i]))