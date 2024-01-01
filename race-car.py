from collections import deque

class Solution:
    def racecar(self, target: int) -> int:
        def get(p, s, cc):
            for c in cc:
                if c == "A":
                    p += s
                    s *= 2
                else:
                    if s > 0:
                        s = -1
                    else:
                        s = 1
            return p, s
        q = deque([(0, 1, 0)])
        v = {(0, 1)}
        while len(q) > 0:
            pos, speed, steps = q.pop()
            if pos == target:
                return steps
            if abs(pos) > 2 * target:
                continue
            for c in ["A", "R"]:
                newpos, newspeed = get(pos, speed, c)
                if (newpos, newspeed) in v:
                    continue 
                v.add((newpos, newspeed))
                q.appendleft((newpos, newspeed, steps + 1))