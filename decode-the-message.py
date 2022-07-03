class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        seen = set()
        cipher = {}
        i = 0
        for c in key:
            if c not in seen and c.isalpha():
                cipher[c] = chr(ord('a') + i)
                i += 1
                seen.add(c)
        return "".join([cipher.get(c, c) for c in message])