class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = 0
        while i < n:
            ctr = 1
            while i < n - 1 and chars[i] == chars[i + 1]:
                i += 1
                ctr += 1
            i += 1
            if ctr == 1:
                chars.extend([chars[i - 1]])
            else:
                chars.extend([chars[i - 1]] + list(str(ctr)))
        for i in range(n):
            chars.pop(0)
        return len(chars)