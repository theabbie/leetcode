n = int(input())

arr = list(map(int, input().split()))

print(*[el for el in arr if el % 2 == 0])