import bisect

class SnapshotArray:
    def __init__(self, length: int):
        self.snaps = {}
        self.sid = 0
        for i in range(length):
            self.snaps[i] = [(0, 0)]

    def set(self, index: int, val: int) -> None:
        self.snaps[index].append((self.sid, val))

    def snap(self) -> int:
        res = self.sid
        self.sid += 1
        return res

    def get(self, index: int, snap_id: int) -> int:
        beg = 0
        end = len(self.snaps[index]) - 1
        res = 0
        while beg <= end:
            mid = (beg + end) // 2
            if self.snaps[index][mid][0] <= snap_id:
                res = self.snaps[index][mid][1]
                beg = mid + 1
            else:
                end = mid - 1
        return res
                