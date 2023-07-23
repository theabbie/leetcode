import bisect

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        n = len(s)
        s = [ord(c) - ord('a') for c in s]
        letter = ord(letter) - ord('a')
        pos = [[] for _ in range(26)]
        for i in range(n):
            pos[s[i]].append(i)
        prev = -1
        rem = repetition
        res = [""] * k
        for i in range(k):
            for c in range(26):
                p = bisect.bisect_right(pos[c], prev)
                if p == len(pos[c]):
                    continue
                j = pos[c][p]
                if k - i > n - j:
                    continue
                newrem = rem - int(c == letter)
                available = bisect.bisect_right(pos[letter], n - 1) - bisect.bisect_left(pos[letter], j + 1)
                if k - i - 1 < newrem:
                    continue
                if available >= newrem:
                    res[i] = chr(ord('a') + c)
                    rem = newrem
                    prev = j
                    break
        return "".join(res)