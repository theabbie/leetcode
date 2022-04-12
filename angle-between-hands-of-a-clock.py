class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        mAngle = minutes * 6
        hAngle = (hour * 30 + minutes / 2) % 360
        diff = abs(mAngle - hAngle)
        return min(diff, 360 - diff)