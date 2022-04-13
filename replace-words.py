class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)
        lens = sorted([len(w) for w in dictionary])
        words = sentence.split()
        op = []
        for w in words:
            found = False
            for l in lens:
                if w[:l] in dictionary:
                    op.append(w[:l])
                    found = True
                    break
            if not found:
                op.append(w)
        return " ".join(op)