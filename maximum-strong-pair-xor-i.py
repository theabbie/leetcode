class Node:
    def __init__(self):
        self.child = [None, None]
        self.ctr = 0

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, s):
        curr = self.root
        curr.ctr += 1
        for c in s:
            c = int(c)
            if curr.child[c] == None:
                curr.child[c] = Node()
            curr = curr.child[c]
            curr.ctr += 1
            
    def delete(self, s):
        curr = self.root
        curr.ctr -= 1
        for c in s:
            c = int(c)
            if curr.child[c] == None:
                curr.child[c] = Node()
            curr = curr.child[c]
            curr.ctr -= 1
        
    def getmax(self, s):
        curr = self.root
        res = 0
        for c in s:
            c = int(c)
            if curr.child[1 - c] != None and curr.child[1 - c].ctr > 0:
                curr = curr.child[1 - c]
                res = 2 * res + 1
            elif curr.child[c] != None and curr.child[c].ctr > 0:
                curr = curr.child[c]
                res = 2 * res
        return res

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        val = lambda x: "{:021b}".format(x)
        nums.sort()
        trie = Trie()
        i = 0
        res = 0
        for j in range(n):
            trie.insert(val(nums[j]))
            while i < j and nums[j] - nums[i] > nums[i]:
                trie.delete(val(nums[i]))
                i += 1
            if nums[j] - nums[i] <= nums[i]:
                res = max(res, trie.getmax(val(nums[j])))
        return res