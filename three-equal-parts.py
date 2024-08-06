class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        if sum(arr) == 0:
            return [0, 2]
        n = len(arr)
        pos = [i for i in range(n) if arr[i] == 1]
        x = len(pos)
        if x % 3 != 0:
            return [-1, -1]
        k = x // 3
        z = 0
        while n - z - 1 >= 0 and arr[n - z - 1] == 0:
            z += 1
        a = arr[: pos[k - 1] + z + 1]
        b = arr[pos[k - 1] + z + 1 : pos[2 * k - 1] + z + 1]
        c = arr[pos[2 * k - 1] + z + 1 :]
        res = [len(a) - 1, len(a) + len(b)]
        a.reverse()
        b.reverse()
        c.reverse()
        while a and a[-1] == 0:
            a.pop()
        while b and b[-1] == 0:
            b.pop()
        while c and c[-1] == 0:
            c.pop()
        if not a == b == c:
            res = [-1, -1]
        return res