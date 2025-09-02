class Solution:
    def kthSmallestProduct(self, a, b, k):
        if len(a) > len(b):
            a, b = b, a
        n = len(b)
        minb, maxb = min(b), max(b)
        offset = -minb
        size = maxb - minb + 1
        freq = [0] * size
        for x in b:
            freq[x + offset] += 1
        pref = [0] * size
        pref[0] = freq[0]
        for i in range(1, size):
            pref[i] = pref[i-1] + freq[i]
        def count(x, up):
            if x == 0:
                return n if up >= 0 else 0
            if x > 0:
                t = up // x
                if t < minb:
                    return 0
                if t >= maxb:
                    return n
                return pref[t + offset]
            q, r = divmod(up, x)
            t = q + (1 if r else 0)
            if t <= minb:
                return n
            if t > maxb:
                return 0
            return n - pref[t - 1 + offset]
        beg = min(a[0] * minb, a[0] * maxb, a[-1] * minb, a[-1] * maxb)
        end = max(a[0] * minb, a[0] * maxb, a[-1] * minb, a[-1] * maxb)
        while beg <= end:
            mid = (beg + end) // 2
            if sum(count(x, mid) for x in a) < k:
                beg = mid + 1
            else:
                end = mid - 1
        return beg