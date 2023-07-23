from collections import Counter, defaultdict

class FreqStack:
    def __init__(self):
        self.freq = Counter()
        self.maxfreq = 0
        self.freqgrp = defaultdict(list)

    def push(self, val: int) -> None:
        newfreq = self.freq[val] + 1
        self.freq[val] = newfreq
        self.maxfreq = max(self.maxfreq, newfreq)
        self.freqgrp[newfreq].append(val)

    def pop(self) -> int:
        val = self.freqgrp[self.maxfreq].pop()
        if len(self.freqgrp[self.maxfreq]) == 0:
            self.maxfreq -= 1
        self.freq[val] -= 1
        return val