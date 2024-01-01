class DataStream:
    def __init__(self, value: int, k: int):
        self.val = -1
        self.eq = 0
        self.value = value
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.val:
            self.eq += 1
        else:
            self.eq = 1
            self.val = num
        return self.val == self.value and self.eq >= self.k