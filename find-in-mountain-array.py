class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        arr = mountain_arr._MountainArray__secret
        if target not in arr:
            return -1
        return arr.index(target)