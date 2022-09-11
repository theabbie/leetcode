class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        n = len(s)
        prev = [None] * 26
        index = lambda c: ord(c) - ord('a')
        for i in range(n):
            if prev[index(s[i])] != None:
                if i - prev[index(s[i])] - 1 != distance[index(s[i])]:
                    return False
            prev[index(s[i])] = i
        return True