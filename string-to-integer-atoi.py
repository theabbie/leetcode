class Solution:
    def clamp(self, val, MIN, MAX):
        if val < MIN:
            return MIN
        if val > MAX:
            return MAX
        return val
    
    def myAtoi(self, s: str) -> int:
        MIN = -1 << 31
        MAX = -MIN - 1
        sign = None
        val = None
        for c in s:
            if c == "+" or c == "-":
                if val != None:
                    break
                if sign == None:
                    sign = [-1, 1][c == "+"]
                else:
                    return 0
            elif 48 <= ord(c) < 58:
                d = ord(c) - 48
                val = 10 * (val or 0) + d
            elif val == None and sign == None:
                if c != " ":
                    return 0
            else:
                break
        return self.clamp((sign or 1) * (val or 0), MIN, MAX)