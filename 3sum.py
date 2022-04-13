class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []
        triplets = set()
        nums.sort()
        for i in range(n - 2):
            a = nums[i]
            start = i + 1
            end = n - 1
            while start < end:
                b = nums[start]
                c = nums[end]
                total = a + b + c
                if total == 0:
                    triplets.add(tuple(sorted([a, b, c])))
                    start += 1
                    end -= 1
                elif total > 0:
                    end -= 1
                else:
                    start += 1
        return [list(triplet) for triplet in triplets]
                            
                        