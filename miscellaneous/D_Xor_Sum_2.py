n = int(input())

arr = list(map(int, input().split()))

last = [-1] * 32

for i in range(n):
    curr = []
    for b in range(32):
        if arr[i] & (1 << b):
            last[b] = i
            curr.append(1)
        else:
            curr.append(0)
    print(curr[:6])
    