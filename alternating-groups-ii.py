class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        for i in range(k - 1):
            colors.append(colors[i])
        n = len(colors)
        res = 0
        last = 0
        for i in range(n - 1, -1, -1):
            if i == n - 1 or colors[i] != colors[i + 1]:
                last += 1
            else:
                last = 1
            if last >= k:
                res += 1
        return res