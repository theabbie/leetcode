n, m = map(int, input().split())

items = []

for _ in range(n):
    curr = list(map(int, input().split()))
    items.append(curr)

def check(items):
    n = len(items)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if items[i][0] < items[j][0]:
                continue
            ifeat = set(items[i][2:])
            jfeat = set(items[j][2:])
            valid = True
            for ii in ifeat:
                if ii not in jfeat:
                    valid = False
                    break
            if not valid:
                continue
            if items[i][0] > items[j][0]:
                return "Yes"
            found = False
            for jj in jfeat:
                if jj not in ifeat:
                    found = True
                    break
            if found:
                return "Yes"
    return "No"

print(check(items))