from collections import Counter

class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        n = len(creators)
        creatorctr = Counter()
        for i in range(n):
            creatorctr[creators[i]] += views[i]
        mviews = max(creatorctr.values())
        rescreators = set([creators[i] for i in range(n) if creatorctr[creators[i]] == mviews])
        mvideo = {}
        for i in range(n):
            if creators[i] not in mvideo:
                mvideo[creators[i]] = (ids[i], views[i])
            else:
                if views[i] > mvideo[creators[i]][1]:
                    mvideo[creators[i]] = (ids[i], views[i])
                elif views[i] == mvideo[creators[i]][1] and ids[i] < mvideo[creators[i]][0]:
                    mvideo[creators[i]] = (ids[i], views[i])
        return [[c, mvideo[c][0]] for c in rescreators]