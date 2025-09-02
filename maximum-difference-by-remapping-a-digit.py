class Solution:
    def minMaxDifference(self, num: int) -> int:
        def remap(v, mp):
            return int(''.join(mp[1] if c == mp[0] else c for c in v))
        num = str(num)
        i = 0
        while i < len(num) and num[i] == '9':
            i += 1
        mx = ('9', '9')
        if i < len(num):
            mx = (num[i], '9')
        mn = (num[0], '0')
        return remap(num, mx) - remap(num, mn)