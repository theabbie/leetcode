# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         k = min([len(s) for s in strs])
#         i = 0
#         while i <= k and len(set([s[:i] for s in strs])) == 1:
#             i += 1
#         return strs[0][:i-1]

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         n = len(strs)
#         prefixes = {}
#         for s in strs:
#             for i in range(len(s) + 1):
#                 prefixes[s[:i]] = prefixes.get(s[:i], 0) + 1
#         return max([(len(k), k, v) for k, v in prefixes.items() if v == n])[1]

# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         k = min([len(s) for s in strs])
#         i = 0
#         while i < k and len(set([s[i] for s in strs])) == 1:
#             i += 1
#         return strs[0][:i]

class Solution:
    def isLCP(self, strs, k):
        return len(set([s[:k] for s in strs])) == 1

    def longestCommonPrefix(self, strs):
        n = len(strs)
        if n == 0:
            return ""
        beg = 0
        end = min([len(s) for s in strs])
        while beg <= end:
            mid = (beg + end) // 2
            currval = self.isLCP(strs, mid)
            nextval = self.isLCP(strs, mid + 1)
            if (currval and not nextval) or mid >= end:
                return strs[0][:mid]
            elif beg == end:
                break
            elif currval and nextval:
                beg = mid + 1
            else:
                end = mid
        return ""