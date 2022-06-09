class SnapshotArray:

    def __init__(self, length: int):
        self.snaps = {}
        self.sid = 0
        self.n = length

    def set(self, index: int, val: int) -> None:
        self.snaps[(self.sid, index)] = val

    def snap(self) -> int:
        res = self.sid
        self.sid += 1
        return res
    
    def getSnap(self, snap_id, index):
        for i in range(snap_id, -1, -1):
            if (i, index) in self.snaps:
                return self.snaps[(i, index)]
        return 0

    def get(self, index: int, snap_id: int) -> int:
        return self.getSnap(snap_id, index)

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)