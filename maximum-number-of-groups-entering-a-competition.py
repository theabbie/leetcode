class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort()
        prev = 0
        prevcount = 0
        curr = 0
        currcount = 0
        res = 0
        for grade in grades:
            curr += grade
            currcount += 1
            if curr > prev and currcount > prevcount:
                prev = curr
                prevcount = currcount
                curr = 0
                currcount = 0
                res += 1
        return res