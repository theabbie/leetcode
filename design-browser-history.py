class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.next = []

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.next = []

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.stack) > 1:
                self.next.append(self.stack.pop())
        return self.stack[-1]

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if len(self.next) > 0:
                self.stack.append(self.next.pop())
        return self.stack[-1]