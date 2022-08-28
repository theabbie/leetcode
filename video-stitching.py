class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        n = len(clips)
        clips.sort()
        dp = [float('inf')] * (time + 1)
        dp[0] = 0
        for beg, end in clips:
            newend = min(end + 1, time + 1)
            for i in range(beg, newend):
                dp[i] = min(dp[i], dp[beg] + 1)
        if dp[time] == float('inf'):
            return -1
        return dp[time]