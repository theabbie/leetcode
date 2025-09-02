class Solution:
    def get(self, arr):
        n = len(arr)
        res = []
        ctr = Counter()
        mx = (0, None)
        for i in range(n):
            ctr[arr[i]] += 1
            mx = max(mx, (ctr[arr[i]], arr[i]))
            if 2 * mx[0] > i + 1:
                res.append(mx[1])
            else:
                res.append(None)
        return res

    def minimumIndex(self, nums: List[int]) -> int:
        a = self.get(nums)
        b = self.get(nums[::-1])
        for i, el in enumerate(a):
            b.pop()
            if b and el == b[-1] and el != None:
                return i
        return -1