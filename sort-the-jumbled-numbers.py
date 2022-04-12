class Solution:
    def mapNum(self, num, mapping):
        op = 0
        for c in str(num):
            op = 10 * op + mapping[int(c)]
        return op
    
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        return sorted(nums, key = lambda num: self.mapNum(num, mapping))