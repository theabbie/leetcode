class Solution:
    def isPossible(self, i, sides, matchsticks, n, total):
        if i >= n:
            return len(set(sides)) == 1
        key = tuple(sorted(sides) + [i])
        if key in self.cache:
            return self.cache[key]
        for j in range(4):
            if 4 * (sides[j] + matchsticks[i]) > total:
                continue
            sides[j] += matchsticks[i]
            curr = self.isPossible(i + 1, sides, matchsticks, n, total)
            if curr:
                self.cache[key] = True
                return True
            else:
                sides[j] -= matchsticks[i]
        self.cache[key] = False
        return False
    
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse = True)
        n = len(matchsticks)
        total = sum(matchsticks)
        self.cache = {}
        sides = [0, 0, 0, 0]
        return self.isPossible(0, sides, matchsticks, n, total)