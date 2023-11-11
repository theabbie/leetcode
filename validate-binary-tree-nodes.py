class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parent = [0] * n
        for i in range(n):
            if leftChild[i] != -1:
                parent[leftChild[i]] += 1
            if rightChild[i] != -1:
                parent[rightChild[i]] += 1
        if parent.count(0) != 1 or parent.count(1) != n - 1:
            return False
        root = parent.index(0)
        stack = [root]
        v = {root}
        while len(stack) > 0:
            curr = stack.pop()
            if leftChild[curr] in v:
                return False
            if rightChild[curr] in v:
                return False
            if leftChild[curr] != -1:
                v.add(leftChild[curr])
                stack.append(leftChild[curr])
            if rightChild[curr] != -1:
                v.add(rightChild[curr])
                stack.append(rightChild[curr])
        return len(v) == n