N = 1 << 16

smallestprimedivisor = {}

for i in range(2, N + 1):
    if i not in smallestprimedivisor:
        smallestprimedivisor[i] = i
    if smallestprimedivisor[i] == i:
        p = i * 2
        while p <= N:
            if p not in smallestprimedivisor:
                smallestprimedivisor[p] = i
            p += i

def factor(n):
    res = []
    while n > 1:
        k = smallestprimedivisor[n]
        res.append(k)
        n = n // k
    return res

while True:
    print(factor(int(input())))