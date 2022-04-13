class Solution:
    def getRLE(self, string):
        n = len(string)
        i = 0
        op = []
        while i <= n - 1:
            ctr = 1
            while i < n - 1 and string[i] == string[i + 1]:
                ctr += 1
                i += 1
            i += 1
            op.append((string[i - 1], ctr))
        return op
    
    def isLongPressedName(self, name: str, typed: str) -> bool:
        namelist = self.getRLE(name)
        typedlist = self.getRLE(typed)
        m = len(namelist) 
        n = len(typedlist)
        if m == n:
            for i in range(m):
                if namelist[i][0] != typedlist[i][0]:
                    return False
                if namelist[i][1] > typedlist[i][1]:
                    return False
            return True
        return False