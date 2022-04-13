class Solution:
    def beautifulArray(self, N):
        return sorted(range(1, N + 1), key=lambda x: bin(x)[:1:-1])