class Solution:
    def numTrips(self, time, t):
        trips = 0
        for el in time:
            trips += t // el
        return trips
    
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        beg = 1
        end = min(time) * totalTrips
        while beg <= end:
            mid = (beg + end) // 2
            currtrips = self.numTrips(time, mid)
            nexttrips = self.numTrips(time, mid + 1)
            if currtrips < totalTrips and nexttrips >= totalTrips:
                return mid + 1
            elif beg == end:
                break
            elif currtrips < totalTrips:
                beg = mid
            else:
                end = mid
        return (beg + end) // 2