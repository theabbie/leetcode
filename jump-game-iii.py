class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        paths = [[start]]
        visited = set()
        while len(paths) > 0:
            curr = paths.pop(0)
            currIndex = curr[-1]
            jump = arr[currIndex]
            if jump == 0:
                return True
            visited.add(currIndex)
            if currIndex - jump >= 0 and (currIndex - jump) not in visited:
                paths.append(path + [currIndex - jump])
            if currIndex + jump <= n - 1 and (currIndex + jump) not in visited:
                paths.append(path + [currIndex + jump])
        return False