class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = (-1, -1)
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if len(set({i,j,k,l})) == 4:
                            h = 10 * arr[i] + arr[j]
                            m = 10 * arr[k] + arr[l]
                            if 0 <= h < 24 and 0 <= m < 60:
                                res = max(res, (h, m))
        if res[0] == -1:
            return ""
        return f"{res[0]//10}{res[0]%10}:{res[1]//10}{res[1]%10}"