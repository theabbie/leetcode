from collections import deque

class Stack:
    def __init__(self, init, func):
        self.stack = deque([(init, init)])
        self.func = func
        
    def push(self, val):
        top, topfunc = self.stack[-1]
        self.stack.append((val, self.func(topfunc, val)))
        
    def empty(self):
        return len(self.stack) <= 1
    
    def size(self):
        return len(self.stack) - 1
        
    def pop(self):
        if not self.empty():
            top, topfunc = self.stack.pop()
            return top
            
    def funcval(self):
        top, topfunc = self.stack[-1]
        return topfunc

class Queue:
    def __init__(self, init, func):
        self.func = func
        self.f = Stack(init, func)
        self.s = Stack(init, func)
        
    def push(self, val):
        self.f.push(val)
        
    def empty(self):
        return self.f.empty() and self.s.empty()
    
    def size(self):
        return self.f.size() + self.s.size()
    
    def pop(self):
        if self.s.empty():
            while not self.f.empty():
                self.s.push(self.f.pop())
        if not self.s.empty():
            return self.s.pop()
                    
    def funcval(self):
        return self.func(self.f.funcval(), self.s.funcval())

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def count(x):
            i = 0
            res = 0
            q = Queue((1 << 33) - 1, lambda a, b: a & b)
            for j in range(n):
                q.push(nums[j])
                while i < j and q.funcval() < x:
                    q.pop()
                    i += 1
                if q.funcval() >= x:
                    res += j - i + 1
            return res
        return count(k) - count(k + 1)