M = 10 ** 9 + 7

n, m = map(int, input().split())
 
ctr = [0] * (m + 1)
ctr[0] = 1
 
for _ in range(n):
  for i in range(1, m + 1):
    ctr[i] += ctr[i - 1]
    ctr[i] %= M

print(ctr[-1])