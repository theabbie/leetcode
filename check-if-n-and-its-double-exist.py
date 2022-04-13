class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort(reverse = True, key = lambda x: x * x)
        exists = set()
        for num in arr:
            if num * 2 in exists:
                return True
            exists.add(num)
        return False