import random

class MyHashMap:

    def __init__(self):
        self.size = 107
        self.arr = [[] for i in range(self.size)]
        
    def hfn(self, key):
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = ((key >> 16) ^ key) * 0x45d9f3b
        key = (key >> 16) ^ key
        return key % self.size

    def put(self, key: int, value: int) -> None:
        self.remove(key)
        self.arr[self.hfn(key)].append((key, value))

    def get(self, key: int) -> int:
        curr = self.arr[self.hfn(key)]
        val = -1
        for k, v in curr:
            if k == key:
                val = v
                break
        return val

    def remove(self, key: int) -> None:
        k = len(self.arr[self.hfn(key)])
        for i in range(k):
            if self.arr[self.hfn(key)][i][0] == key:
                del self.arr[self.hfn(key)][i]
                break

hashmap = MyHashMap()

n = 1000

for i in range(n):
    hashmap.put(random.randint(0, n), random.randint(0, n))

print([len(item) for item in hashmap.arr])