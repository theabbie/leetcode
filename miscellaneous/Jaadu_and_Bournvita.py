from collections import defaultdict, deque

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())

arr = list(map(int, input().split()))

M = max(arr)
 
ctr = [0] * (M + 1)
 
for el in arr:
  ctr[el] += 1
 
mulctr = [0] * (M + 1)
 
res = 1
found = False
 
i = M
 
while i >= 1:
  j = i
  while j <= M:
    mulctr[i] += ctr[j]
    j += i
  i -= 1

res = n

for i in range(n):
    res = min(res, n - mulctr[arr[i]])
    for j in range(i + 1, n):
        x = arr[i] * arr[j] // gcd(arr[i], arr[j])
        res = min(res, n - (mulctr[arr[i]] + mulctr[arr[j]] - (mulctr[x] if x <= M else 0)))

print(res)