class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()
        nxt = [n] * n
        for i in range(n):
            beg = i + 1
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                if intervals[mid][0] > intervals[i][1]:
                    end = mid - 1
                else:
                    beg = mid + 1
            nxt[i] = end + 1
        dp = [[(0, tuple())] * 5 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for rem in range(5):
                a, avals = dp[i + 1][rem]
                b, bvals = dp[nxt[i]][rem - 1] if rem > 0 else (float('-inf'), tuple())
                b += intervals[i][2]
                if a > b:
                    dp[i][rem] = a, avals
                else:
                    bvals = sorted(tuple([intervals[i][3]] + list(bvals)))
                    if b > a:
                        dp[i][rem] = b, bvals
                    else:
                        dp[i][rem] = a, min(avals, bvals)
        return dp[0][4][1]