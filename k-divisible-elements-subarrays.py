class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        subs = set()
        left, right, divs = 0, 0, 0
        while right < len(nums):
            if nums[right] % p == 0:
                divs += 1
            while divs > k and left < right:
                if nums[left] % p == 0:
                    divs -= 1
                left += 1
            for l in range(left, right + 1):
                subs.add(tuple(nums[l:right + 1]))
            right += 1
        return len(subs)