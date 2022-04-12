class Solution:
    def numMatchingSubseq(self, s: str, words) -> int:
        pos = {}
        for i, c in enumerate(s):
            pos[c] = pos.get(c, [])  + [i]
        valid = []
        for word in words:
            isValid = True
            curr = []
            for c in word:
                if c in pos:
                    curr.append(pos[c])
                else:
                    isValid = False
                    break
            if isValid:
                paths = [[i] for i in curr[0]]
                i = 0
                while i < len(paths):
                    currpath = paths[i]
                    if len(currpath) == len(word):
                        valid.append(word)
                        break
                    for j in curr[len(currpath)]:
                        if j > currpath[-1]:
                            curr.append(currpath + [j])
                    i += 1
            else:
                continue
        return len(valid)

print(Solution().numMatchingSubseq("abcde", ["ace"]))