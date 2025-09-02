class Solution:
    def earliestAndLatest(self, n, f, s):
        f -= 1
        s -= 1
        f0, s0 = f, s
        start = (1 << n) - 1
        min_r = n + 1
        max_r = 0
        stack = [(start, 1)]
        seen = set()
        while stack:
            mask, r = stack.pop()
            if mask in seen:
                continue
            seen.add(mask)
            if not ((mask >> f0) & 1 and (mask >> s0) & 1):
                continue
            alive = [i for i in range(n) if (mask >> i) & 1]
            m = len(alive)
            pairs = []
            i, j = 0, m - 1
            while i < j:
                pairs.append((alive[i], alive[j]))
                i += 1
                j -= 1
            mid = alive[i] if i == j else None
            meet = False
            for x, y in pairs:
                if {x, y} == {f0, s0}:
                    if r < min_r:
                        min_r = r
                    if r > max_r:
                        max_r = r
                    meet = True
                    break
            if meet:
                continue
            next_masks = [0]
            for x, y in pairs:
                tmp = []
                if {x, y} != {f0, s0}:
                    for m0 in next_masks:
                        tmp.append(m0 | (1 << x))
                        tmp.append(m0 | (1 << y))
                else:
                    for m0 in next_masks:
                        tmp.append(m0 | (1 << f0))
                next_masks = tmp
            if mid is not None:
                for k in range(len(next_masks)):
                    next_masks[k] |= (1 << mid)
            for nm in next_masks:
                stack.append((nm, r + 1))
        return [min_r, max_r]