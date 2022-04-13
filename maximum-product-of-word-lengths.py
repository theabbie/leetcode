class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        lens = [len(word) for word in words]
        words = [set(word) for word in words]
        mprod = 0
        for i in range(n):
            for j in range(n):
                if i != j:
                    if len(set.intersection(words[i], words[j])) == 0:
                        mprod = max(mprod, lens[i] * lens[j])
        return mprod