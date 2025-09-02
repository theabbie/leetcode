class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        LOG = n.bit_length() + 1
        p = [0] * (n + 1)
        for i in range(n):
            p[i + 1] = p[i] + nums[i]
        parent = [[i] * LOG for i in range(n + 1)]
        ops = [[0] * LOG for i in range(n + 1)]
        nxt = [n] * n
        stack = []
        for i in range(n):
            while stack and nums[i] >= nums[stack[-1]]:
                nxt[stack.pop()] = i
            stack.append(i)
        for i in range(n):
            ops[i][0] = nums[i] * (nxt[i] - i) - (p[nxt[i]] - p[i])
            parent[i][0] = nxt[i]
        for l in range(1, LOG):
            for i in range(n):
                ops[i][l] = ops[i][l - 1] + ops[parent[i][l - 1]][l - 1]
                parent[i][l] = parent[parent[i][l - 1]][l - 1]
        res = 0
        for i in range(n):
            j = i
            curr = 0
            for b in range(LOG - 1, -1, -1):
                if curr + ops[j][b] <= k:
                    curr += ops[j][b]
                    j = parent[j][b]
            if j == n:
                res += j - i
                continue
            beg = j
            end = nxt[j] - 1
            while beg <= end:
                mid = (beg + end) // 2
                if curr + nums[j] * (mid - j + 1) - (p[mid + 1] - p[j]) <= k:
                    beg = mid + 1
                else:
                    end = mid - 1
            res += beg - i
        return res
            