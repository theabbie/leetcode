from functools import cmp_to_key

class Solution:
    def distance(self, a, b):
        return (b[0] - a[0]) * (b[0] - a[0]) + (b[1] - a[1]) * (b[1] - a[1])
    
    def orientation(self, a, b, c):
        return (b[1] - a[1]) * (c[0] - b[0]) - (b[0] - a[0]) * (c[1] - b[1])
    
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        n = len(trees)
        if n <= 1:
            return trees
        beg = min(trees)
        def cmp(a, b):
            d = self.orientation(beg, a, b) - self.orientation(beg, b, a)
            if d == 0:
                return self.distance(beg, a) - self.distance(beg, b)
            return 1 if d > 0 else -1
        trees.sort(key = cmp_to_key(cmp))
        i = n - 1
        while i >= 0 and self.orientation(beg, trees[-1], trees[i]) == 0:
            i -= 1
        j = i + 1
        k = n - 1
        while j < k:
            trees[j], trees[k] = trees[k], trees[j]
            j += 1
            k -= 1
        stack = []
        stack.append(trees[0])
        stack.append(trees[1])
        for i in range(2, n):
            curr = stack.pop()
            while self.orientation(stack[-1], curr, trees[i]) > 0:
                curr = stack.pop()
            stack.append(curr)
            stack.append(trees[i])
        return stack