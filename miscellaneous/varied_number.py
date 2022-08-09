t = int(input())

def getNum(s, prev):
    if s < 0:
        return None
    if s == 0:
        return ""
    minVal = float('inf')
    for i in range(prev + 1, 10):
        curr = getNum(s - i, i)
        if curr != None:
            currval = str(i) + curr
            minVal = min(minVal, int(currval))
    if minVal == float('inf'):
        return None
    return str(minVal)

for _ in range(t):
    s = int(input())
    print(getNum(s, 0))