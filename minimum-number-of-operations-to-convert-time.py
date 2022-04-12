class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        bhh, bmm = [int(x) for x in current.split(":")]
        ehh, emm = [int(x) for x in correct.split(":")]
        diff = (ehh - bhh) * 60 + (emm - bmm)
        ctr = 0
        while diff > 0:
            if diff >= 60:
                ctr += diff // 60
                diff = diff % 60
            elif diff >= 15:
                ctr += diff // 15
                diff = diff % 15
            elif diff >= 5:
                ctr += diff // 5
                diff = diff % 5
            else:
                ctr += diff
                break
        return ctr