class Solution:
    def maxHeightOfTriangle(self, r: int, b: int) -> int:
        def h(red, blue):
            res = 0
            while True:
                if res % 2 == 0:
                    if blue >= res + 1:
                        blue -= res + 1
                    else:
                        break
                else:
                    if red >= res + 1:
                        red -= res + 1
                    else:
                        break
                res += 1
            return res
        return max(h(r, b), h(b, r))