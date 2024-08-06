class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        res = []
        prev = (0, 0)
        for i, c in enumerate(target):
            pos = ord(c) - ord('a')
            curr = (pos // 5, pos % 5)
            px, py = prev
            cx, cy = curr
            def xmove():
                nonlocal px, cx
                while px < cx:
                    res.append('D')
                    px += 1
                while px > cx:
                    res.append('U')
                    px -= 1
            def ymove():
                nonlocal py, cy
                while py < cy:
                    res.append('R')
                    py += 1
                while py > cy:
                    res.append('L')
                    py -= 1
            if c == 'z':
                ymove()
                xmove()
            else:
                xmove()
                ymove()
            res.append('!')
            prev = curr
        return "".join(res)