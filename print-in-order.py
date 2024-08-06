class Foo:
    def __init__(self):
        self.f = False
        self.s = False

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.f = True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.f:
            pass
        printSecond()
        self.s = True

    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.f or not self.s:
            pass
        printThird()