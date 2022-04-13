class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        s += fill * (n % k if n % k == 0 else k - n % k)
        n = len(s)
        op = []
        for i in range(0, n, k):
            op.append(s[i:i+k])
        return op