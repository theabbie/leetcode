class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        nums.sort()
        def check(ops):
            req = 0
            for el in [el - y * ops for el in nums if el - y * ops > 0]:
                req += math.ceil(el / (x - y))
            return req <= ops
        end = 1
        while not check(end):
            end *= 2
        beg = end // 2
        while beg <= end:
            mid = (beg + end) // 2
            if check(mid):
                end = mid - 1
            else:
                beg = mid + 1
        return end + 1