def absolutePermutation(n, k):
    if 2 * k > n:
        return [-1]
    if k == 0:
        return list(range(1, n + 1))
    perms = [[k+i+1 for i in range(k)]]
    while len(perms) > 0:
        curr = perms.pop(0)
        if len(curr) == n:
            return curr
        pos = len(curr) + 1
        if (pos - k) >= 1 and (pos - k) not in curr:
            perms.append(curr + [pos - k])
        if (pos + k) <= n and (pos + k) not in curr:
            perms.append(curr + [pos + k])
    return [-1]

print(absolutePermutation(100, 30))