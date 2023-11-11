class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res = []
        vals = []
        cons = 0
        prev = -1
        for el in words:
            if el == "prev":
                if prev == "prev":
                    cons += 1
                else:
                    cons = 1
                if len(vals) < cons:
                    res.append(-1)
                else:
                    res.append(vals[-cons])
            else:
                vals.append(int(el))
            prev = el
        return res