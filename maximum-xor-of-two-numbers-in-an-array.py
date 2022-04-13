class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        maxx = 0
        mask = 0
        se = set()
        for i in range(30, -1, -1):
            mask |= (1 << i)
            newMaxx = maxx | (1 << i)
            for i in range(n):
                se.add(nums[i] & mask)
            for prefix in se:
                if (newMaxx ^ prefix) in se:
                    maxx = newMaxx
                    break
            se.clear()
        return maxx