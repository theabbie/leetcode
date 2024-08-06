class MyHashSet:
    def __init__(self):
        self.x = set()

    def add(self, key: int) -> None:
        self.x.add(hash(key))

    def remove(self, key: int) -> None:
        if hash(key) in self.x:
            self.x.remove(hash(key))

    def contains(self, key: int) -> bool:
        return hash(key) in self.x