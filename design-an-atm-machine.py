from collections import defaultdict

class ATM:

    def __init__(self):
        self.notectr = defaultdict(int)

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.notectr[[20, 50, 100, 200, 500][i]] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        currnotectr = self.notectr.copy()
        for note in [500, 200, 100, 50, 20]:
            notesused = min(amount // note, currnotectr[note])
            amount -= notesused * note
            currnotectr[note] -= notesused
            if amount == 0:
                break
        if amount != 0:
            return [-1]
        used = [self.notectr[note] - currnotectr[note] for note in [20, 50, 100, 200, 500]]
        self.notectr = currnotectr
        return used
            


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)