class Solution:
    def coinChangeRec(self, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in self.memo:
            return self.memo[amount]
        numCoins = float('inf')
        for coin in self.coins:
            currMin = 1 + self.coinChangeRec(amount - coin)
            if currMin == 0:
                continue
            numCoins = min(numCoins, currMin)
        if numCoins == float('inf'):
            numCoins = -1
        self.memo[amount] = numCoins
        return numCoins
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {}
        self.coins = coins
        return self.coinChangeRec(amount)