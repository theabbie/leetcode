class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validPairs = ['()', '[]', '{}']
        valid = True
        for bracket in s:
            if bracket in [b[0] for b in validPairs]:
                stack.append(bracket)
            else:
                if len(stack) > 0:
                    if (stack.pop() + bracket) not in validPairs:
                        valid = False
                        break
                else:
                    valid = False
                    break
        if len(stack) > 0:
            valid = False
        return valid