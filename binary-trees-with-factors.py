class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arrset = set(arr)
        arr = sorted(arrset)
        n = len(arr)
        count = {}
        res = 0
        for num in arr:
            ctr = 1
            i = 0
            while arr[i] * arr[i] <= num:
                if num % arr[i] == 0 and num // arr[i] in arrset:
                    l = count[arr[i]]
                    r = count[num // arr[i]]
                    k = 1
                    if arr[i] * arr[i] != num:
                        k = 2
                    ctr += k * l * r
                i += 1
            count[num] = ctr
            res += ctr
        return res % (10 ** 9 + 7)