from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        s = deque(students)
        sw = deque(sandwiches)
        ss = sum(s)
        while s:
            if s[0] == sw[0]:
                ss -= s.popleft()
                sw.popleft()
            else:
                s.append(s.popleft())
                if ss == 0 or ss == len(s):
                    break
        return len(s)