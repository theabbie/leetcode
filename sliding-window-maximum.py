class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
        self.ctr = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, s):
        curr = self.root
        curr.ctr += 1
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.ctr += 1
        curr.end = True
        
    def delete(self, s):
        curr = self.root
        curr.ctr -= 1
        for c in s:
            curr = curr.child[c]
            curr.ctr -= 1
        curr.end = True

    def check(self, s):
        curr = self.root
        for c in s:
            if c not in curr.child or curr.child[c].ctr == 0:
                return False
            curr = curr.child[c]
        return curr.end
    
    def kthsmallest(self, k):
        curr = self.root
        res = 0
        while True:
            done = True
            for c in sorted(curr.child):
                if k > curr.child[c].ctr:
                    k -= curr.child[c].ctr
                else:
                    res = 10 * res + int(c)
                    curr = curr.child[c]
                    done = False
                    break
            if done:
                break
        return res

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        M = min(nums)
        M = -M if M < 0 else 0
        trie = Trie()
        for i in range(n):
            trie.insert("{:010}".format(M + nums[i]))
            if i >= k:
                trie.delete("{:010}".format(M + nums[i - k]))
            if i >= k - 1:
                res.append(trie.kthsmallest(k) - M)
        return res