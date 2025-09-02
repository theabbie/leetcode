from collections import defaultdict

class SHash:
    def __init__(self, input_string: str):
        self.input_string = input_string
        self.prime1 = 31
        self.prime2 = 37
        self.mod1 = 10**9 + 7
        self.mod2 = 10**9 + 9
        self.precompute_hashes()
        
    def precompute_hashes(self):
        n = len(self.input_string)
        self.hash1 = [0] * (n + 1)
        self.hash2 = [0] * (n + 1)
        self.pow1 = [1] * (n + 1)
        self.pow2 = [1] * (n + 1)
        
        for i in range(n):
            self.hash1[i + 1] = (self.hash1[i] * self.prime1 + ord(self.input_string[i])) % self.mod1
            self.hash2[i + 1] = (self.hash2[i] * self.prime2 + ord(self.input_string[i])) % self.mod2
            self.pow1[i + 1] = (self.pow1[i] * self.prime1) % self.mod1
            self.pow2[i + 1] = (self.pow2[i] * self.prime2) % self.mod2
            
    def hash(self, start: int, end: int):
        hash_val1 = (self.hash1[end + 1] - self.hash1[start] * self.pow1[end - start + 1]) % self.mod1
        hash_val2 = (self.hash2[end + 1] - self.hash2[start] * self.pow2[end - start + 1]) % self.mod2
        
        return (hash_val1, hash_val2)

class Solution:
    def jump(self, nums):
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            if nxt <= r:
                return -1
            l, r = r, nxt
        return times
    
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        arr = [0] * (n + 1)
        groups = defaultdict(set)
        for w in words:
            shash = SHash(w)
            m = len(w)
            for l in range(1, m + 1):
                groups[l].add(shash.hash(0, l - 1))
        shash = SHash(target)
        for i in range(n - 1, -1, -1):
            beg = 1
            end = n - i
            while beg <= end:
                mid = (beg + end) // 2
                if shash.hash(i, i + mid - 1) in groups[mid]:
                    beg = mid + 1
                else:
                    end = mid - 1
            arr[i] = beg - 1
        return self.jump(arr)