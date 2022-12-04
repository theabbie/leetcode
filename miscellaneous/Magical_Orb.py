M = 998244353

n, m = map(int, input().split())

res = 0

def pow(a, b):
  curr = a
  res = 1
  while b:
    if b & 1:
      res = (res * curr) % M
    b = b >> 1
    curr = (curr * curr) % M
  return res

for i in range(1, m + 1):
    x = "{:b}".format(i).count("1")
    res = (res + pow((1 << x) - 1, n - 1)) % M

print(res)