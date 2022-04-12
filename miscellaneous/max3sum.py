class Solution:
    def maxSumDivThree(self, nums):
        msum = 0
        n = len(nums)
        rem = { 0: [], 1: [], 2: [] }
        for num in nums:
            rem[num % 3].append(num)
        print(rem)
        msum += sum(rem[0])
        msum2 = msum
        rem[1].sort(reverse = True)
        rem[2].sort(reverse = True)
        k = min(len(rem[1]), len(rem[2]))
        for i in range(k):
            msum2 += (rem[1][i] + rem[2][i])
        msum += sum(rem[1][:len(rem[1]) - len(rem[1]) % 3])
        rem[1] = rem[1][len(rem[1]) - len(rem[1]) % 3 :]
        msum += sum(rem[2][:len(rem[2]) - len(rem[2]) % 3])
        rem[2] = rem[2][len(rem[2]) - len(rem[2]) % 3 :]
        k = min(len(rem[1]), len(rem[2]))
        for i in range(k):
            msum += (rem[1][i] + rem[2][i])
        return max(msum, msum2)

print(Solution().maxSumDivThree([2,19,6,16,5,10,7,4,11,6]))