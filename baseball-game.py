class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score = [0]
        for op in ops:
            if op == "+":
                score.append(score[-1] + score[-2])
            elif op == "C":
                score.pop()
            elif op == "D":
                score.append(score[-1] << 1)
            else:
                score.append(int(op))
        return sum(score)