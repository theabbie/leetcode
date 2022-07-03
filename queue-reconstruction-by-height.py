class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        people.sort()
        res = [-1] * n
        for h, k in people:
            ctr = k
            for j in range(n):
                if res[j] == -1 and ctr == 0:
                    res[j] = [h, k]
                    break
                elif res[j] == -1 or res[j][0] >= h:
                    ctr -= 1
        return res