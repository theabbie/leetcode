f=open('user.out','w')
for height in map(loads, stdin):
    n = len(height)
    i = 0
    j = n - 1
    H = max(height)
    res = 0
    for h in range(H + 1):
        while i < n and height[i] < h:
            i += 1
        while j >= 0 and height[j] < h:
            j -= 1
        if i < j:
            res = max(res, h * (j - i))
    print(res, file = f)
exit(0)