class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse = True)
        used = 0
        curr = 0
        for el in capacity:
            curr += el
            used += 1
            if curr >= s:
                return used
        return -1