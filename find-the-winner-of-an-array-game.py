class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        i = 0
        winctr = 0
        prev = -1
        while i < len(arr) - 1:
            winner = max(arr[i], arr[i + 1])
            if winner == prev:
                winctr += 1
            else:
                winctr = 1
            if winctr >= k:
                return winner
            arr.append(min(arr[i], arr[i + 1]))
            arr[i + 1] = max(arr[i], arr[i + 1])
            prev = winner
            i += 1