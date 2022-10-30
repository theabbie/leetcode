import math

n, x = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort()

rem = 0

for i in range(2, x + 1):
    