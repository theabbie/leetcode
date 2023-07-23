m, n = map(int, input().split())

res = []

for _ in range(m):
    arr = list(map(int, input().split()))
    res.append("".join("." if el == 0 else chr(ord('A') + el - 1) for el in arr))

print("\n".join(res))