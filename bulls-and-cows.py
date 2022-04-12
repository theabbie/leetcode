class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        unused = {}
        bulls = 0
        cows = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                unused[secret[i]] = unused.get(secret[i], 0) + 1
        for i in range(n):
            if secret[i] != guess[i]:
                if guess[i] in unused:
                    cows += 1
                    unused[guess[i]] -= 1
                    if unused[guess[i]] == 0:
                        del unused[guess[i]]
        return "{}A{}B".format(bulls, cows)