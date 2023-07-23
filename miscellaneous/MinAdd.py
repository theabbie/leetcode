t = int(input())

def smallest(num, i, n, used, tight, k, curr, c):
  if i >= n:
    return int(curr)
  key = (i, used, tight)
  if key in c:
    return c[key]
  mindigit = 0
  if tight:
    mindigit = int(num[i])
  res = float('inf')
  for d in range(mindigit, 10):
    newused = used | (1 << d)
    if "{:b}".format(newused).count("1") <= k:
      res = smallest(num, i + 1, n, newused, tight and (d == mindigit), k, curr + str(d), c)
      if res < float('inf'):
        break
  c[key] = res
  return res

for _ in range(t):
    n, k = input().split()
    k = int(k)
    print(smallest(n, 0, len(n), 0, True, k, "", {}) - int(n))