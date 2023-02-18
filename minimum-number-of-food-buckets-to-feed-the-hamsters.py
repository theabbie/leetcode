class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)
        n = len(hamsters)
        res = 0
        for i in range(n):
            valid = False
            if hamsters[i] == "H":
                if i > 0 and hamsters[i - 1] == "B":
                    valid = True
                if not valid:
                    res += 1
                    if i < n - 1 and hamsters[i + 1] == ".":
                        hamsters[i + 1] = "B"
                    elif i > 0 and hamsters[i - 1] == ".":
                        hamsters[i - 1] = "B"
                    else:
                        return -1
        return res