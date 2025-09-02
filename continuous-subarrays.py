class Stack:
    def __init__(self, init, func):
        self.stack = deque([(init, init)])
        self.func = func
        
    def push(self, val):
        top, topfunc = self.stack[-1]
        self.stack.append((val, self.func(topfunc, val)))
        
    def empty(self):
        return len(self.stack) <= 1
        
    def pop(self):
        if not self.empty():
            top, topfunc = self.stack.pop()
            return top
            
    def funcval(self):
        top, topfunc = self.stack[-1]
        return topfunc

class Queue:
    def __init__(self, init = float('inf'), func = min):
        self.func = func
        self.f = Stack(init, func)
        self.s = Stack(init, func)
        
    def push(self, val):
        self.f.push(val)
        
    def empty(self):
        return self.f.empty() and self.s.empty()
    
    def pop(self):
        if self.s.empty():
            while not self.f.empty():
                self.s.push(self.f.pop())
        if not self.s.empty():
            return self.s.pop()
                    
    def funcval(self):
        return self.func(self.f.funcval(), self.s.funcval())

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        minq = Queue(float('inf'), func = min)
        maxq = Queue(float('-inf'), func = max)
        i = 0
        for j in range(n):
            minq.push(nums[j])
            maxq.push(nums[j])
            while i < j and maxq.funcval() - minq.funcval() > 2:
                minq.pop()
                maxq.pop()
                i += 1
            res += j - i + 1
        return res