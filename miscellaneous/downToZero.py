import math

cache = {}

def downToZero(n):
    if n <= 3:
        return n
    if n in cache:
        return cache[n]
    a = 1 + downToZero(n - 1)
    minFac = float('inf')
    for k in range(0, n - 1):
        val = math.sqrt(4 * n + k * k)
        if val % 1 == 0:
            minFac = min(minFac, 1 + downToZero(int((k + val) / 2)))
    cache[n] = min(a, minFac)
    return cache[n]

# try:
#     downToZero(10)
# except:
#     print(cache)

# def downToZero(n):
#     m = int(n / 2)
#     vals = [i for i in range(1, n + 1)]
#     vals[0] = 0
#     vals[1] = 1
#     vals[2] = 2
#     vals[3] = 3
#     for i in range(n + 1):
#         for j in range(i + 1, n + 1):
#             if i * j <= n:
#                 vals[i * j] = min(vals[i * j], 1 + vals[j])
#     for i in range(n):
#         vals[i + 1] = min(vals[i + 1], 1 + vals[i])
#     print(vals)

print(downToZero(1000))