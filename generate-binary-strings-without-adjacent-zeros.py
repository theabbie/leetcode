class Solution:
    def validStrings(self, n: int) -> List[str]:
        def valid(s):
            for i in range(n - 1):
                if s[i] == '0' and s[i + 1] == '0':
                    return False
            return True
        return [("{:0"+str(n)+"b}").format(x) for x in range(1 << n) if valid(("{:0"+str(n)+"b}").format(x))]