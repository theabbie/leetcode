import heapq

class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.deleted = {}

    def push(self, val: int) -> None:
        heapq.heappush(self.heap, val)
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack.pop()
        self.deleted[popped] = self.deleted.get(popped, 0) + 1
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        curr = self.heap[0]
        while curr in self.deleted:
            heapq.heappop(self.heap)
            self.deleted[curr] -= 1
            if self.deleted[curr] == 0:
                del self.deleted[curr]
            curr = self.heap[0]
        return curr


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()