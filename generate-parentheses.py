class Solution:
    def generate(self, s, ctr, rem, ans):
        if rem == 0 and ctr == 0:
            ans.add(s)
        if rem > 0 and ctr >= 0:
            if ctr < rem:
                self.generate(s + '(', ctr + 1, rem - 1, ans)
            if ctr > 0:
                self.generate(s + ')', ctr - 1, rem - 1, ans)
    
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        self.generate("", 0, 2 * n, ans)
        return list(ans)