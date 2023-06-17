class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        beg = 0
        end = n - 1
        res = letters[0]
        while beg <= end:
            mid = (beg + end) // 2
            if letters[mid] > target:
                res = letters[mid]
                end = mid - 1
            else:
                beg = mid + 1
        return res