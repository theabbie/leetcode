import heapq

class SeatManager:
    def __init__(self, n: int):
        self.unreserved = []
        for s in range(1, n + 1):
            heapq.heappush(self.unreserved, s)

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)