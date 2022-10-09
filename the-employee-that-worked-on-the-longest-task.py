class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        memp = 0
        mtime = 0
        prev = 0
        for eid, t in logs:
            if t - prev > mtime:
                mtime = t - prev
                memp = eid
            elif t - prev == mtime and eid < memp:
                memp = eid
            prev = t
        return memp