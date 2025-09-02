import numpy as np

class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        def auction_algorithm(w):
            n = len(w)
            epsilon = 1 / (n + 1)
            prices = np.zeros(n)
            assignment = -np.ones(n, dtype=int)
            while np.any(assignment == -1):
                for student in range(n):
                    if assignment[student] != -1:
                        continue
                    net_benefits = w[student] - prices
                    best_mentor = np.argmax(net_benefits)
                    best_value = net_benefits[best_mentor]
                    net_benefits[best_mentor] = -np.inf
                    second_best_value = np.max(net_benefits)
                    prices[best_mentor] += best_value - second_best_value + epsilon
                    for other_student, mentor in enumerate(assignment):
                        if mentor == best_mentor:
                            assignment[other_student] = -1
                            break
                    assignment[student] = best_mentor
            total_weight = sum(w[student, mentor] for student, mentor in enumerate(assignment))
            return int(total_weight)
        n = len(students)
        w = np.zeros((n, n), dtype=int)
        for i in range(n):
            for j in range(n):
                for k in range(len(students[i])):
                    if students[i][k] == mentors[j][k]:
                        w[i][j] += 1
        return auction_algorithm(w)