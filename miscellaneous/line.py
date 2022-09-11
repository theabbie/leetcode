t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    nums = []
    score = 0
    for i in range(n):
        mscore = max(i, n - i - 1)
        if s[i] == "L":
            if i < mscore:
                nums.append((n - i - 1, i))
            else:
                score += i
        else:
            if n - i - 1 < mscore:
                nums.append((i, n - i - 1))
            else:
                score += n - i - 1
    nums.sort(reverse = True)
    total = 0
    for a, b in nums:
        total += b
    curr = 0
    for k in range(n):
        if k < len(nums):
            a, b = nums[k]
            curr += a
            total -= b
        print(score + curr + total, end = " ")
    print()