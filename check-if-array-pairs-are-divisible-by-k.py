class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        ctr = [0] * k
        for el in arr:
            ctr[el % k] += 1
        for i in range(1, k):
            if ctr[i] != ctr[k - i]:
                return False
        return ctr[0] % 2 == 0