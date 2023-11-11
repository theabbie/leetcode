class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount % 10 >= 5:
            purchaseAmount += 10 - purchaseAmount % 10
        else:
            purchaseAmount -= purchaseAmount % 10
        return 100 - purchaseAmount