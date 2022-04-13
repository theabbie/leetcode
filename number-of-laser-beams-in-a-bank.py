class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        bank = [b for b in bank if int(b) != 0]
        val = 0
        n = len(bank)
        for i in range(n - 1):
            val += bank[i].count("1") * bank[i + 1].count("1")
        return val