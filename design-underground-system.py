from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.cins = {}
        self.paths = defaultdict(int)
        self.pathctr = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        st, ot = self.cins[id]
        self.paths[(st, stationName)] += t - ot
        self.pathctr[(st, stationName)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        k = (startStation, endStation)
        return self.paths[k] / self.pathctr[k]