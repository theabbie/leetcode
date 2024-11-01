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
    
class SegmentTree:
    def __init__(self, data, default=float('inf'), func=min):
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        n = len(target)
        dp = SegmentTree([float('inf')] * (n + 1))
        dp[n] = 0
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
            if beg - 1 > 0:
                dp[i] = min(dp[i], 1 + dp.query(i + 1, i + beg))
        if dp[0] == float('inf'):
            return -1
        return dp[0]