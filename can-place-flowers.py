class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        fctr = 0
        i = 0
        seen = False
        while i < m:
            ctr = 1
            while i < m - 1 and flowerbed[i] == flowerbed[i + 1]:
                i += 1
                ctr += 1
            if flowerbed[i] == 0:
                if seen and i < m - 1:
                    fctr += (ctr - 1) // 2
                elif seen or i < m - 1:
                    fctr += ctr // 2
                else:
                    fctr += (ctr + 1) // 2
            else:
                seen = True
            i += 1
        return fctr >= n