class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        beg = 0
        end = n - 1
        while beg <= end:
            mid = (beg + end) // 2
            if mid < n - 1 and letters[mid] <= target and letters[mid + 1] > target:
                return letters[mid + 1]
            elif beg == end:
                if mid < n - 1:
                    return letters[mid]
                else:
                    return letters[0]
            elif letters[mid] > target:
                end = mid
            else:
                beg = mid + 1