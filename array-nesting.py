class Solution:
    def DFS(self, nums, i, visited):
        visited.add(i)
        if nums[i] not in visited:
            return self.DFS(nums, nums[i], visited)
        else:
            return (i, visited)
    
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        mlen = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                start, l = self.DFS(nums, i, set())
                end, l = self.DFS(nums, start, set())
                visited.update(l)
                mlen = max(mlen, len(l))
        return mlen