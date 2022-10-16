class Solution:
    def countTime(self, time: str) -> int:
        hres = 0
        mres = 0
        h = time[0:2]
        m = time[3:5]
        for i in range(24):
            s = "0" * (1 if i < 10 else 0) + str(i)
            match = True
            for j in range(2):
                if h[j] != '?' and s[j] != h[j]:
                    match = False
                    break
            if match:
                hres += 1
        for i in range(60):
            s = "0" * (1 if i < 10 else 0) + str(i)
            match = True
            for j in range(2):
                if m[j] != '?' and s[j] != m[j]:
                    match = False
                    break
            if match:
                mres += 1
        return hres * mres