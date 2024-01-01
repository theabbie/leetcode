from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        times = defaultdict(list)
        res = []
        for emp, time in access_times:
            times[emp].append(time)
        for emp in list(times):
            times[emp].sort()
        for emp in times:
            curr = times[emp]
            m = len(curr)
            for i in range(m - 2):
                h1 = int(curr[i][:2])
                m1 = int(curr[i][-2:])
                h2 = int(curr[i + 2][:2])
                m2 = int(curr[i + 2][-2:])
                diff = (60 * h2 + m2) - (60 * h1 + m1)
                if diff < 60:
                    res.append(emp)
                    break
        return res