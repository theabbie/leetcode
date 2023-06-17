class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.cap = [big, medium, small]
        self.ctr = [0, 0, 0]

    def addCar(self, carType: int) -> bool:
        if self.ctr[carType - 1] + 1 <= self.cap[carType - 1]:
            self.ctr[carType - 1] += 1
            return True
        return False