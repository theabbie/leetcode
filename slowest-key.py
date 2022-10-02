class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(keysPressed)
        releaseTimes.append(0)
        i = max(range(n), key = lambda j: (releaseTimes[j] - releaseTimes[j - 1], keysPressed[j]))
        return keysPressed[i]