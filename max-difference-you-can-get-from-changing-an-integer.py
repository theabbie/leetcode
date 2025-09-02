class Solution:
    def maxDiff(self, num: int) -> int:
        def remap(v, mp):
            return int(''.join(mp[1] if c == mp[0] else c for c in v))
        num = str(num)
        i = 0
        while i < len(num) and num[i] == '9':
            i += 1
        mx = ('9', '9')
        if i < len(num):
            mx = (num[i], '9')
        i = 0
        while i < len(num) and int(num[i]) <= 1:
            i += 1
        mn = ('0', '0')
        if i < len(num):
            mn = (num[i], '0')
        if int(num[0]) > 1:
            mn = (num[0], '1')
        return remap(num, mx) - remap(num, mn)