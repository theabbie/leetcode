from collections import Counter

n = int(input())

arr = list(map(int, input().split()))

ctr = Counter(arr)

arr = sorted(ctr.items())

