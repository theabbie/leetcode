import random

arr = [random.randint(0, 100) for i in range(20)]

seg = {}

def makeSeg(arr, i, j):
    if (i, j) in seg:
        return seg[(i, j)]
    if i == j:
        seg[(i, j)] = arr[i]
        return arr[i]
    mid = (i + j) // 2
    curr = min(makeSeg(arr, i, mid), makeSeg(arr, mid + 1, j))
    seg[(i, j)] = curr
    return curr

makeSeg(arr, 0, len(arr) - 1)

for key in seg:
    print("{:02d} - {:02d} -> {:02d}".format(key[0], key[1], seg[key]))

def getMin(arr, i, j, ni, nj):
    if ni >= i and nj <= j:
        return seg[(ni, nj)]
    if (ni < i and nj < i) or (ni > j and nj > j):
        return float('inf')
    mid = (ni + nj) // 2
    return min(getMin(arr, i, j, ni, mid), getMin(arr, i, j, mid + 1, nj))
