class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        booked = [0] * (n + 1)
        for l, r, ctr in bookings:
            booked[l - 1] += ctr
            booked[r] -= ctr
        for i in range(1, n + 1):
            booked[i] += booked[i - 1]
        booked.pop()
        return booked