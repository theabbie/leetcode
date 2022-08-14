t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(range(1, n + 1))
    for i in range(n - 2, -1, -2):
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    print(*nums)