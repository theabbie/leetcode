class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [b.count("1") for b in bank if b.count("1") != 0]
        val = 0
        n = len(bank)
        for i in range(n - 1):
            val += bank[i] * bank[i + 1]
        return val