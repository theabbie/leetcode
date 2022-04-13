class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indices)
        op = list(s)
        for i in range(n):
            if s[indices[i]:indices[i]+len(sources[i])] == sources[i]:
                op[indices[i]] = targets[i]
                for j in range(indices[i] + 1, indices[i] + len(sources[i])):
                    op[j] = ""
        return "".join(op)