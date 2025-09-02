class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        res = []
        for el in arr:
            if el == 0:
                res.append(0)
                res.append(0)
            else:
                res.append(el)
        for i in range(len(arr)):
            arr[i] = res[i]
        return arr