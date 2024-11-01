class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        ctr = [0] * 26
        rem = [0] * 26
        pos = lambda x: ord(x) - ord('a')
        chars = {pos(c) for c in s}
        def check(extra, gone):
            for i in chars:
                if ctr[i] + rem[i] + int(extra == i) - int(gone == i) == 0:
                    return False
            return True
        for c in s:
            rem[pos(c)] += 1
        for c in s:
            rem[pos(c)] -= 1
            if ctr[pos(c)] > 0:
                continue
            while stack and stack[-1] > c and check(pos(c), pos(stack[-1])):
                p = stack.pop()
                ctr[pos(p)] -= 1
            ctr[pos(c)] += 1
            stack.append(c)
        return "".join(stack)