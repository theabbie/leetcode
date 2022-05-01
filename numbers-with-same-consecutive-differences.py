class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        nums = list(range(1, 10))
        op = set()
        visited = set()
        while len(nums) > 0:
            curr = nums.pop()
            currlen = len(str(curr))
            if currlen == n:
                op.add(curr)
            d = curr % 10
            if currlen < n:
                for nd in [d - k, d + k]:
                    if 0 <= nd <= 9:
                        newcurr = 10 * curr + nd
                        if newcurr not in visited:
                            visited.add(newcurr)
                            nums.append(newcurr)
        return list(op)