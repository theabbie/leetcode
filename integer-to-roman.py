class Solution:
    def intToRoman(self, num: int) -> str:
        sym = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M"
        }
        keys = list(sym.keys())
        k = len(keys)
        vals = []
        i = 1
        while num > 0:
            curr = num % (10 ** i)
            vals.insert(0, curr)
            num -= curr
            i += 1
        print(vals)
        op = ""
        curr = 0
        while curr < len(vals):
            v = vals[curr]
            if v in sym:
                op += sym[v]
            else:
                found = False
                for i in range(k):
                    for j in range(i + 1, k):
                        if v == keys[j] - keys[i]:
                            found = True
                            op += sym[keys[i]] + sym[keys[j]]
                            break
                if not found:
                    for key in keys[::-1]:
                        if v > key:
                            op += sym[key] * (v // key)
                            vals.insert(curr + 1, v % key)
                            break
            curr += 1
        return op