class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        n = len(coins)
        coins.sort()
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + coins[i][2] * (coins[i][1] - coins[i][0] + 1)
        starts = set()
        for l, r, c in coins:
            starts.add(l)
            starts.add(r - k + 1)
        res = 0
        starts = sorted(starts)
        for s in starts:
            l = s
            r = s + k - 1
            beg = 0
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                if coins[mid][0] >= l:
                    end = mid - 1
                else:
                    beg = mid + 1
            first = end + 1
            beg = 0
            end = n - 1
            while beg <= end:
                mid = (beg + end) // 2
                if coins[mid][1] <= r:
                    beg = mid + 1
                else:
                    end = mid - 1
            last = beg - 1
            curr = 0
            if first <= last:
                curr += p[last + 1] - p[first]
            if first - 1 >= 0:
                if coins[first - 1][1] >= l:
                    curr += (coins[first - 1][1] - s + 1) * coins[first - 1][2]
            if last + 1 < n and last + 1 != first - 1:
                if coins[last + 1][0] <= r:
                    curr += (r - coins[last + 1][0] + 1) * coins[last + 1][2]
            res = max(res, curr)
        return res