class Heap:
    def __init__(self):
        self.heap = []

    def siftup(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def siftdown(self, i):
        while True:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            smallest = i

            if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child

            if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def __len__(self):
        return len(self.heap)

    def push(self, val):
        self.heap.append(val)
        self.siftup(len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        res = self.heap.pop()
        self.siftdown(0)
        return res

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = Heap()
        for el in nums:
            heap.push(el)
            if len(heap) > k:
                heap.pop()
        return heap.pop()