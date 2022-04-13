class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        n = len(pattern)
        pattCaps = "".join([c for c in pattern if c.isupper()])
        answer = []
        for q in queries:
            m = len(q)
            qCaps = "".join([c for c in q if c.isupper()])
            if pattCaps != qCaps:
                answer.append(False)
                continue
            i = 0
            j = 0
            while i < n and j < m:
                if pattern[i] == q[j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            answer.append(i == n)
        return answer