t = int(input())

N = 2 * 10 ** 5
P1 = 10 ** 9 + 7
P2 = 10 ** 9 + 9
M1 = 10 ** 9 + 33
M2 = 10 ** 9 + 21
PINV1 = pow(P1 - 1, M1 - 2, M1)
PINV2 = pow(P2 - 1, M2 - 2, M2)
P1POWS = [1] * (N + 1)
P2POWS = [1] * (N + 1)
for i in range(N):
    P1POWS[i + 1] = (P1 * P1POWS[i]) % M1
    P2POWS[i + 1] = (P2 * P2POWS[i]) % M2

def getprefhash(s, pows, M):
    n = len(s)
    psum = [0] * (n + 1)
    for i in range(n):
        psum[i + 1] += psum[i] + pows[i] * int(s[i])
        psum[i + 1] %= M
    return psum

def gethash(val, i, j, pows, M, pinv):
    return (val + (M + pows[j + 1] - pows[i]) * pinv) % M

for _ in range(t):
    n, m = map(int, input().split())
    hashes = set()
    s = input()
    fhash = getprefhash(s, P1POWS, M1)
    shash = getprefhash(s, P2POWS, M2)
    p = [0] * (n + 1)
    for i in range(n):
        p[i + 1] += p[i] + int(s[i])
    for _ in range(m):
        l, r = map(int, input().split())
        l -= 1
        r -= 1
        currfhash = (M1 + fhash[l] + fhash[n] - fhash[r + 1]) % M1
        currshash = (M2 + shash[l] + shash[n] - shash[r + 1]) % M2
        ones = p[r + 1] - p[l]
        zeroes = r - l + 1 - ones
        currfhash = gethash(currfhash, l + zeroes, r, P1POWS, M1, PINV1)
        currshash = gethash(currshash, l + zeroes, r, P2POWS, M2, PINV2)
        hashes.add((currfhash, currshash))
    print(len(hashes))