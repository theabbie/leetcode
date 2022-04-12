import bisect

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        checkins = {}
        for i in range(n):
            name = keyName[i]
            time = keyTime[i]
            time = tuple(int(k) for k in time.split(":"))
            if name in checkins:
                bisect.insort(checkins[name], time)
            else:
                checkins[name] = [time]
        op = []
        for name in sorted(checkins.keys()):
            m = len(checkins[name])
            alert = False
            for i in range(m):
                curr = checkins[name][i]
                j = bisect.bisect_right(checkins[name], (curr[0] + 1, curr[1]))
                if j - i >= 3:
                    alert = True
                    break
            if alert:
                op.append(name)
        return op