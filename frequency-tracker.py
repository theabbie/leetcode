from collections import Counter

class FrequencyTracker:
    def __init__(self):
        self.freq = Counter()
        self.freqfreq = Counter()

    def add(self, number: int) -> None:
        self.freqfreq[self.freq[number]] -= 1
        self.freq[number] += 1
        self.freqfreq[self.freq[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.freq[number] > 0:
            self.freqfreq[self.freq[number]] -= 1
            self.freq[number] -= 1
            self.freqfreq[self.freq[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freqfreq[frequency] > 0