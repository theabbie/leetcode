t = int(input())

def getD(c):
    i = int(c)
    j = min(i + 1, 9)
    return str(j)

def merge(nums1, m, nums2, n):
    while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    if n > 0:
        nums1[:n] = nums2[:n]

for _ in range(t):
    s = input()
    n = len(s)
    minc = "9"
    d = []
    rem = []
    for i in range(n - 1, -1, -1):
        minc = min(minc, s[i])
        if s[i] <= minc:
            d.append(s[i])
        else:
            rem.append(getD(s[i]))
    d.reverse()
    rem.sort()
    d.extend([0] * len(rem))
    merge(d, len(d) - len(rem), rem, len(rem))
    print("".join(d))