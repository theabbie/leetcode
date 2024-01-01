class WordFilter:
    def __init__(self, words: List[str]):
        self.vals = {}
        for pos in range(len(words)):
            n = len(words[pos])
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    self.vals[(words[pos][:i], words[pos][n-j:])] = pos

    def f(self, pref: str, suff: str) -> int:
        return self.vals.get((pref, suff), -1)