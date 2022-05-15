class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        stack = []
        for w in words:
            if len(stack) == 0 or sorted(w) != sorted(stack[-1]):
                stack.append(w)
        return stack