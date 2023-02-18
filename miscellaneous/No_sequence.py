t = int(input())

def getseq(n, k, s):
    seq = []
    for _ in range(n):
        seq.append(s % k)
        s //= k
    return seq[::-1]

for _ in range(t):
    n, k, s = map(int, input().split())
    seq = getseq(n, k, s)
    res = []
    carry = 1
    for i in range(n):
        curr = (seq[i] + carry) // k
        if curr == k - 1:
            res.append(-1)
        else:
            res.append(curr)
        carry = (seq[i] + carry) % k
    print(res)