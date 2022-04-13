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


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)