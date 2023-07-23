n = int(input())

arr = list(map(int, input().split()))

arr.sort()

print(sum(arr[n:-n]) / (3 * n))