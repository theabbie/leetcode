class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        res = 0
        for i in range(len(fruits)):
            j = 0
            while j < len(baskets) and baskets[j] < fruits[i]:
                j += 1
            if j < len(baskets):
                baskets[j] = 0
            else:
                res += 1
        return res