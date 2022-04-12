class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        ctr = 0
        i, j = 0, n - 1
        while i <= j:
            ctr += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ctr