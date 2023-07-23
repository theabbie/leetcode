t = int(input())

resprint = []

def intersect(a, b, c, k):
    return (b - k) * (b - k) - 4 * a * c >= 0

for _ in range(t):
    n, m = map(int, input().split())
    slopes = []
    for _ in range(n):
        slopes.append(int(input()))
    slopes.sort()
    curves = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        curves.append((a, b, c))
    for a, b, c in curves:
        beg = 0
        end = n - 1
        res = -1
        while beg <= end:
            mid = (beg + end) // 2
            if intersect(a, b, c, slopes[mid]):
                x = -b / (2 * a)
                x *= abs(2 * a)
                y = a * x * x + b * x + c
                if x * slopes[mid] > y:
                    end = mid - 1
                elif x * slopes[mid] < y:
                    beg = mid + 1
                else:
                    for j in [mid - 1, mid + 1]:
                        if 0 <= j < n and not intersect(a, b, c, slopes[j]):
                            res = j
                            break
                    break
            else:
                res = mid
                break
        if res == -1:
            resprint.append("NO")
        else:
            resprint.append("YES")
            resprint.append(slopes[res])

print("\n".join(map(str, resprint)))