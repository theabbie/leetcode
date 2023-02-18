from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq = {}
        self.freqmap = defaultdict(OrderedDict)
        self.minfreq = float('inf')

    def get(self, key: int) -> int:
        if key not in self.freq:
            return -1
        freq = self.freq[key]
        val = self.freqmap[freq][key]
        del self.freqmap[freq][key]
        if not self.freqmap[freq]:
            if freq == self.minfreq:
                self.minfreq += 1
            del self.freqmap[freq]
        self.freq[key] += 1
        self.freqmap[freq + 1][key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.freq:
            freq = self.freq[key]
            self.freqmap[freq][key] = value
            self.get(key)
            return
        if len(self.freq) == self.capacity:
            evictkey, evictval = self.freqmap[self.minfreq].popitem(last = False)
            del self.freq[evictkey]
        self.freq[key] = 1
        self.freqmap[1][key] = value
        self.minfreq = 1