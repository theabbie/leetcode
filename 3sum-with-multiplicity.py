class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        d = [0] * 300
        res = 0
        for i, el in enumerate(arr):
            res += d[target - el] if target - el >= 0 else 0
            for j in range(i):
                d[el + arr[j]] += 1
        return res % (10 ** 9 + 7)