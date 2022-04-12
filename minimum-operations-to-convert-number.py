class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        paths = [(start, 0)]
        visited = {start}
        i = 0
        while i < len(paths):
            curr, steps = paths[i]
            if curr == goal:
                return steps
            if 0 <= curr <= 1000:
                for num in nums:
                    if (curr + num) not in visited:
                        visited.add((curr + num))
                        paths.append((curr + num, steps + 1))
                    if (curr - num) not in visited:
                        visited.add((curr - num))
                        paths.append((curr - num, steps + 1))
                    if (curr ^ num) not in visited:
                        visited.add((curr ^ num))
                        paths.append((curr ^ num, steps + 1))
            i += 1
        return -1