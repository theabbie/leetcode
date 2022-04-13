class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1:
            return s
        op = ""
        for i in range(numRows):
            curr = i
            down = True
            while curr < n:
                op += s[curr]
                if down:
                    if numRows - i - 1 > 0:
                        curr += 2 * (numRows - i - 1)
                    else:
                        curr += 2 * i
                else:
                    if i > 0:
                        curr += 2 * i
                    else:
                        curr += 2 * (numRows - i - 1)
                down = not down
        return op