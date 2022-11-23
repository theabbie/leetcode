h, m = map(int, input().split())

def isValid(hh, mm):
    return 0 <= hh < 24 and 0 <= mm < 60

def getTime(h, m):
    for hh in range(h, 24):
        for mm in range(60):
            if (hh > h and mm >= 0) or (hh == h and mm >= m):
                ha, hb = hh // 10, hh % 10
                ma, mb = mm // 10, mm % 10
                if isValid(10 * ha + ma, 10 * hb + mb):
                    return (hh, mm)
    return (0, 0)

print(*getTime(h, m))