class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = max(length, width, height) >= 10000 or length * width * height  >= 10 ** 9
        heavy = mass >= 100
        if bulky and heavy:
            return "Both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        return "Neither"