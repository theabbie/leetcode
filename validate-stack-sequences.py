class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        n = len(popped)
        i = 0
        j = 0
        stack = []
        while j < n:
            while len(stack) == 0 or stack[-1] != popped[j]:
                if i >= n:
                    return False
                stack.append(pushed[i])
                i += 1
            stack.pop()
            j += 1
        return True