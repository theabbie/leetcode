class TextEditor:

    def __init__(self):
        self.s = ""
        self.c = 0

    def addText(self, text: str) -> None:
        self.s = self.s[:self.c] + text + self.s[self.c:]
        self.c += len(text)

    def deleteText(self, k: int) -> int:
        k = min(k, self.c)
        self.s = self.s[:self.c - k] + self.s[self.c:]
        self.c -= k
        return k

    def cursorLeft(self, k: int) -> str:
        self.c  = max(self.c - k, 0)
        k = min(self.c, 10)
        return self.s[self.c - k : self.c]

    def cursorRight(self, k: int) -> str:
        self.c  = min(self.c + k, len(self.s))
        k = min(self.c, 10)
        return self.s[self.c - k : self.c]


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)