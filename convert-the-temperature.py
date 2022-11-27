class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        f = 1.8 * celsius + 32.0
        k = 273.15 + celsius
        return [k, f]