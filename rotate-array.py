class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = n - k % n
        gcd = self.gcd(k, n)
        for i in range(gcd):
            temp = nums[i]
            j = i
            while 1:
                l = j + k
                if l >= n:
                    l = l - n
                if l == i:
                    break
                nums[j] = nums[l]
                j = l
            nums[j] = temp
        return nums