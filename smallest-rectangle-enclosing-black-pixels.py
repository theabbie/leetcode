class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m = len(image)
        n = len(image[0])
        stack = [(x, y)]
        v = {(x, y)}
        mnx = mxx = x
        mny = mxy = y
        while stack:
            i, j = stack.pop()
            mnx = min(mnx, i)
            mny = min(mny, j)
            mxx = max(mxx, i)
            mxy = max(mxy, j)
            for ii, jj in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:
                if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in v and image[ii][jj] == "1":
                    v.add((ii, jj))
                    stack.append((ii, jj))
        return (mxy - mny + 1) * (mxx - mnx + 1)