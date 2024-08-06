def compute_lps(pattern):
    length = 0
    lps = [0] * len(pattern)
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps

def find_pattern_indices(string, pattern):
    indices = []
    n = len(string)
    m = len(pattern)
    lps = compute_lps(pattern)
    i = j = 0

    while i < n:
        if string[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                indices.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        vals = [("A" if nums[i + 1] > nums[i] else ("B" if nums[i + 1] < nums[i] else "C")) for i in range(n - 1)]
        vals = "".join(vals)
        pattern = "".join(["A" if el == 1 else ("B" if el == -1 else "C") for el in pattern])
        return len(find_pattern_indices(vals, pattern))