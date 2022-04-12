from collections import Counter

class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.maxfreq = 0
        self.freqgrp = {}

    def push(self, val: int) -> None:
        newfreq = self.freq[val] + 1
        self.freq[val] = newfreq
        self.maxfreq = max(self.maxfreq, newfreq)
        self.freqgrp[newfreq] = self.freqgrp.get(newfreq, []) + [val]

    def pop(self) -> int:
        val = self.freqgrp[self.maxfreq].pop()
        if len(self.freqgrp[self.maxfreq]) == 0:
            self.maxfreq -= 1
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()