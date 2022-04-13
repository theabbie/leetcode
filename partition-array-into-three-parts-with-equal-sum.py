class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        total = sum(arr)
        curr = 0
        first = []
        second = []
        for i in range(n):
            curr += arr[i]
            if curr * 3 == total:
                first.append(i)
            if curr * 3 == 2 * total:
                second.append(i)
        for f in first:
            for s in second:
                if s < n - 1 and f < s:
                    return True
        return False