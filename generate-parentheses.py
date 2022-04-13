class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        pars = [("(", [1])]
        ans = []
        i = 0
        while i < len(pars):
            curr, currstack = pars[i]
            if len(curr) == 2 * n and len(currstack) == 0:
                ans.append(curr)
            if len(curr) < 2 * n:
                if len(currstack) > 0 and currstack[-1] == 1:
                    pars.append((curr + ")", currstack[:-1]))
                pars.append((curr + "(", currstack + [1]))
            i += 1
        return ans