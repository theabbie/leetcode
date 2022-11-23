n = int(input())

arr = list(map(int, input().split()))

allsame = None
changed = set()

q = int(input())

for _ in range(q):
    curr = list(map(int, input().split()))
    if curr[0] == 1:
        allsame = curr[1]
        changed.clear()
    elif curr[0] == 2:
        if allsame != None and curr[1] not in changed:
            arr[curr[1] - 1] = curr[2] + allsame
            changed.add(curr[1])
        else:
            arr[curr[1] - 1] += curr[2]
    else:
        if allsame != None and curr[1] not in changed:
            print(allsame)
        else:
            print(arr[curr[1] - 1])