class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        n = len(report)
        pf = set(positive_feedback)
        nf = set(negative_feedback)
        def score(s):
            res = 0
            for w in s.split():
                if w in pf:
                    res += 3
                if w in nf:
                    res -= 1
            return res
        seq = sorted(range(n), key = lambda i: (-score(report[i]), student_id[i]))
        return [student_id[seq[i]] for i in range(k)]