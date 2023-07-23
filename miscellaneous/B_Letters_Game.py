from collections import Counter

n, m = map(int, input().split())

arr = list(map(int, input().split()))

vals = sorted(Counter(arr).values())

j = len(vals) - 1

i = 0

done = 0

while i < n:
    if vals[i] == 0:
        i += 1
    if vals[j] == 0:
        j -= 1
    
    if j > i and vals[j] > 0:
        vals[i] -= 1
        vals[j] -= 1
        done += 1

print(done)

print("YES" if done == n else "NO")