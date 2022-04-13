"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def DFS(self, employees, i, visited):
        visited.add(i)
        for j in employees[i][1]:
            if j not in visited:
                self.DFS(employees, j, visited)
    
    def getImportance(self, employees: List['Employee'], i: int) -> int:
        empMap = {}
        for emp in employees:
            empMap[emp.id] = [emp.importance, emp.subordinates]
        visited = set()
        self.DFS(empMap, i, visited)
        return sum([empMap[k][0] for k in visited])