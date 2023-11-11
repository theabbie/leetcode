class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        c = [0] * (n + 1)
        for i in range(n):
            a[i + 1] += a[i]
            b[i + 1] += b[i]
            c[i + 1] += c[i]
            if nums[i] == 1:
                a[i + 1] += 1
            if nums[i] == 2:
                b[i + 1] += 1
            if nums[i] == 3:
                c[i + 1] += 1
        res = n
        for aa in range(n + 1):
            for bb in range(n + 1 - aa):
                cc = n - aa - bb
                curr = (b[aa] + c[aa]) + (a[aa + bb] - a[aa] + c[aa + bb] - c[aa]) + (a[aa + bb + cc] - a[aa + bb] + b[aa + bb + cc] - b[aa + bb])
                res = min(res, curr)
        return res