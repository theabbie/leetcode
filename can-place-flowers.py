class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        fn = len(flowerbed)
        for i in range(fn):
            if flowerbed[i] == 0:
                isValid = True
                if i > 0 and flowerbed[i - 1] == 1:
                    isValid = False
                if i < fn - 1 and flowerbed[i + 1] == 1:
                    isValid = False
                if isValid:
                    flowerbed[i] = 1
                    n = max(n - 1, 0)
        return n == 0