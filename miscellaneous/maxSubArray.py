def maxSubArray(nums):
    n = len(nums)
    start = 0
    end = start
    currSum = nums[start]
    maxSum = currSum
    while start < n - 1:
        end += 1
        front = nums[end]
        currSum += front
        maxSum = max(maxSum, currSum)
        if end == n - 1:
            start += 1
            end = start
            currSum = nums[start]
            maxSum = max(maxSum, currSum)
    return maxSum