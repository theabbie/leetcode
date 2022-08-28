class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n = len(target)
        k = len(stamp)
        res = []
        target = list(target)
        last = ['?'] * n
        while target != last:
            changed = False
            for i in range(n - k + 1):
                valid = True
                charseen = False
                for j in range(i, i + k):
                    if target[j] != '?':
                        charseen = True
                        if target[j] != stamp[j - i]:
                            valid = False
                if valid and charseen:
                    changed = True
                    res.append(i)
                    for j in range(i, i + k):
                        target[j] = '?'
            if not changed:
                return []
        if len(res) > 10 * n:
            return []
        return res[::-1]