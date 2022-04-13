class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s += " "
        token = ""
        curr = None
        for c in s:
            if c == " ":
                if token.isdigit():
                    if curr:
                        if int(token) <= curr:
                            return False
                    curr = int(token)
                token = ""
            else:
                token += c
        return True