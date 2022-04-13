class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        k = min([len(s) for s in strs])
        i = 0
        while i <= k and len(set([s[:i] for s in strs])) == 1:
            i += 1
        return strs[0][:i-1]