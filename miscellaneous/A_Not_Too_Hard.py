n, x = map(int, input().split())

arr = list(map(int, input().split()))

print(sum(el for el in arr if el <= x))