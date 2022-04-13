class Solution:
    def maximum69Number (self, num: int) -> int:
        currmax = num
        numstr = str(num)
        if '6' in numstr:
            i = numstr.index('6')
            curr = int(numstr[0:i] + '9' + numstr[i+1:])
            currmax = max(currmax, curr)
        return currmax