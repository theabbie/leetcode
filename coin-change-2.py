class Solution:
    def ways(self, amount, coins, i, n):
        if amount < 0:
            return 0
        if amount == 0:
            return 1
        key = (amount, i)
        if key in self.cache:
            return self.cache[key]
        ctr = 0
        for j in range(i, n):
            ctr += self.ways(amount - coins[j], coins, j, n)
        self.cache[key] = ctr
        return ctr
    
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort(reverse = True)
        self.cache = {}
        return self.ways(amount, coins, 0, n)