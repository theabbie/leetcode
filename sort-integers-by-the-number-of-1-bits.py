class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        p = 25
        buckets = [[] for i in range(p)]
        for num in arr:
            curr = num
            onebits = 0
            while curr > 0:
                if curr % 2 == 1:
                    onebits += 1
                curr //= 2
            buckets[onebits].append(num)
        op = []
        for b in buckets:
            op += sorted(b)
        return op