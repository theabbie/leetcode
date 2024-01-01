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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def count(self, nums, k):
        q = Queue(0, gcd)
        res = 0
        for el in nums:
            q.push(el)
            while not q.empty() and q.funcval() <= k:
                q.pop()
            res += q.size()
        return res
    
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        return self.count(nums, k - 1) - self.count(nums, k)