class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        n = len(enemyEnergies)
        enemyEnergies.sort(reverse = True)
        if currentEnergy < enemyEnergies[-1]:
            return 0
        for i in range(n - 1):
            currentEnergy += enemyEnergies[i]
        return currentEnergy // enemyEnergies[-1]