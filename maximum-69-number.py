class Solution:
    def maximum69Number (self, num: int) -> int:
        numstr = str(num)
        n = len(numstr)
        currmax = num
        for i in range(n):
            if numstr[i] == '6':
                curr = int(numstr[0:i] + '9' + numstr[i+1:])
                currmax = max(curr, currmax)
        return currmax