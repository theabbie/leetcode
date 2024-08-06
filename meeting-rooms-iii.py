import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        rooms = list(range(n))
        waiting = []
        ctr = [0] * n
        meetings.sort()
        for a, b in meetings:
            while len(waiting) > 0 and waiting[0][0] <= a:
                t, room = heapq.heappop(waiting)
                heapq.heappush(rooms, room)
            slot = a
            if len(rooms) == 0:
                slot, room = heapq.heappop(waiting)
            else:
                room = heapq.heappop(rooms)
            ctr[room] += 1
            heapq.heappush(waiting, (slot + b - a, room))
        return ctr.index(max(ctr))