import heapq

class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)
        freq = [[0, n] for i in range(26)]
        beg = ord('a')
        for i in range(n):
            freq[ord(s[i]) - beg][0] += 1
            freq[ord(s[i]) - beg][1] = min(i, freq[ord(s[i]) - beg][1])
        uniques = [el for el in freq if el[0] == 1]
        k = len(uniques)
        if k > 0:
            unique = min(uniques, key = lambda el: el[1])
            return unique[1]
        return -1