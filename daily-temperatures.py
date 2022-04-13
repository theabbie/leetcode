class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0 for i in range(n)]
        stack = []
        for i in range(n):
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                curr = stack.pop()
                answer[curr] = i - curr
            stack.append(i)
        return answer