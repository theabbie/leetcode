"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        op = []
        for x in range(1, 1001):
            beg = 1
            end = 1000
            while beg <= end:
                y = (beg + end) // 2
                val =  customfunction.f(x, y)
                if val == z:
                    op.append([x, y])
                    break
                elif beg == end:
                    break
                elif val > z:
                    end = y
                else:
                    beg = y + 1
        return op