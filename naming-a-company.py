from collections import Counter

class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        names = set(ideas)
        groups = [[] for _ in range(26)]
        groupctr = Counter()
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].append(idea)
        for l in 'abcdefghijklmnopqrstuvwxyz':
            for c in 'abcdefghijklmnopqrstuvwxyz':
                for pair in groups[ord(l) - ord('a')]:
                    if (c + pair[1:]) not in names:
                        groupctr[(l, c)] += 1
        ctr = 0
        for idea in ideas:
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if (c + idea[1:]) not in names:
                    ctr += groupctr[(c, idea[0])]
        return ctr