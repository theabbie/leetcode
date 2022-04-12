def search(nums, target):
    n = len(nums)
    k = n - 2
    while nums[k] < nums[k + 1] and k >= 0:
        k -= 1
    k = (n - k - 1) % n
    beg = 0
    end = n - 1
    while beg <= end:
        mid = (beg + end) // 2
        print(beg, end, mid)
        if nums[mid - k] == target:
            return (n + mid - k) % n
        elif nums[mid - k] < target:
            beg = mid + 1
        else:
            end = mid
    return -1

print(search([4, 5, 6, 7, 0, 1, 2], 3))