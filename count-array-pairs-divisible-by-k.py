from collections import *

MAX = 1 + 10 ** 5

f = [[] for _ in range(MAX)]

for i in range(1, MAX):
    j = 1
    while i * j < MAX:
        f[i * j].append(i)
        j += 1

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
        
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        res = 0
        ctr = Counter()
        for el in nums:
            res += ctr[k // gcd(el, k)]
            for x in f[el]:
                ctr[x] += 1
        return res