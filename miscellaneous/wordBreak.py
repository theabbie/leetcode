# class Solution:
#     def wordBreak(self, s: str, wordDict):
#         newDict = set()
#         for word in wordDict:
#             newDict.add(word)
#         n = len(s)
#         curr = ""
#         for i in range(n):
#             curr += s[i]
#             if curr in newDict:
#                 if s[i + 1:] in newDict:
#                     return True
#                 curr = ""
#         if len(curr) == 0:
#             return True
#         return False

# class Solution:
#     def wordBreak(self, s: str, wordDict):
#         options = [[s]]
#         while len(options) > 0:
#             curr = options.pop(0)
#             currword = curr.pop()
#             for word in wordDict:
#                 if currword.startswith(word):
#                     if currword == word:
#                         return True
#                     rest = [currword[len(word):]] if len(currword) > len(word) else []
#                     options.append(curr + [word] + rest)
#         return False

# class Solution:
#     def wordBreak(self, s: str, wordDict):
#         n = len(s)
#         wordSet = set()
#         mlen = 0
#         for word in wordDict:
#             wordSet.add(word)
#             mlen = max(mlen, len(word))
#         options = [([""], 0)]
#         while len(options) > 0:
#             curr, beg = options.pop(0)
#             if beg >= n - 1:
#                 return True
#             nword = ""
#             for c in s[beg : beg + mlen]:
#                 nword += c
#                 if nword in wordSet:
#                     options.append((curr + [nword], beg + len(nword)))
#         return False

class Solution:
    def wordBreakRec(self, s, beg, end, wordSet):
        n = len(s)
        if s[beg:end] in wordSet:
            return True
        for i in range(beg, end):
            if self.wordBreakRec(s, beg, i, wordSet) and self.wordBreakRec(s, i, end, wordSet):
                return True
        return False

    def wordBreak(self, s: str, wordDict):
        n = len(s)
        wordSet = set()
        for word in wordDict:
            wordSet.add(word)
        return self.wordBreakRec(s, 0, n, wordSet)

print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))