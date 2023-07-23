class Solution:
    def find(self, people, i, n, curr, skills):
        if i >= n:
            if curr & skills != skills:
                return float('inf')
            return 0
        key = (i, curr)
        if key in self.cache:
            return self.cache[key]
        a = self.find(people, i + 1, n, curr, skills)
        b = 1 + self.find(people, i + 1, n, curr | people[i], skills)
        res = min(a, b)
        self.cache[key] = res
        return res
    
    def smallestSufficientTeam(self, skills, people):
        n = len(people)
        mp = {}
        for s in skills:
            mp[s] = 0
        for p in people:
            for s in p:
                mp[s] = 0
        for i, el in enumerate(sorted(mp)):
            mp[el] = i
        skills = sum(1 << mp[el] for el in skills)
        for p in range(n):
            people[p] = sum(1 << mp[el] for el in people[p])
        self.cache = {}
        res = []
        curr = (0, 0)
        for i in range(n):
            if self.find(people, curr[0] + 1, n, curr[1], skills) <= self.find(people, curr[0] + 1, n, curr[1] | people[i], skills):
                curr = (curr[0] + 1, curr[1])
            else:
                res.append(i)
                curr = (curr[0] + 1, curr[1] | people[i])
        return res