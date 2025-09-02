class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        og = 0
        flowers.sort()
        while flowers and flowers[-1] >= target:
            og += full
            flowers.pop()
        n = len(flowers)
        rem = newFlowers
        def maxmin():
            beg = 0
            end = len(flowers) - 1
            while beg <= end:
                mid = (beg + end) // 2
                if ops[mid] <= rem:
                    beg = mid + 1
                else:
                    end = mid - 1
            return flowers[beg - 1] + (rem - ops[beg - 1]) // beg if flowers else 0
        ops = [0] * n
        s = 0
        for i in range(n):
            s += flowers[i]
            ops[i] = (i + 1) * flowers[i] - s
        res = partial * min(maxmin(), target - 1) + og
        fullscore = 0
        for _ in range(n):
            use = min(rem, max(target - flowers[-1], 0))
            rem -= use
            if flowers[-1] + use >= target:
                fullscore += full
                flowers.pop()
                partialscore = partial * min(maxmin(), target - 1)
                res = max(res, og + fullscore + partialscore)
            else:
                break
        return res