import time

def square(n):
    if n == 0 or n == 1:
        return n
    if n & 1:
        k = (n - 1) >> 1
        return (square(k) << 2) + (k << 2) + 1
    k = n >> 1
    return square(k) << 2

def mul(a, b):
    if a > b:
        a, b = b, a
    k = b - a
    if k & 1:
        return mul(a, b + 1) - a
    k = k >> 1
    return square(a + k) - square(k)

# a = int(input())
# b = int(input())

# print()

# start = time.time()
# print(a * b)
# end = time.time()
# print((end - start) * 10000)

# print()

# start = time.time()
# print(mul(a, b))
# end = time.time()
# print((end - start) * 10000)

n = int(input())

print()

start = time.time()
print(n * n)
end = time.time()
print((end - start) * 10000)

print()

start = time.time()
print(square(n))
end = time.time()
print((end - start) * 10000)