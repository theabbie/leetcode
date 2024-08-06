class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        x = purchaseAmount % 10
        if x < 5:
            purchaseAmount -= x
        else:
            purchaseAmount += 10 - x
        return 100 - purchaseAmount