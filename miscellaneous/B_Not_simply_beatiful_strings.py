from collections import Counter

s = input()

ctr = Counter(s)

def check(ctr):
    if len(ctr) == 4:
        return "Yes"
    if len(ctr) > 4:
        return "No"
    if len(ctr) == 1:
        return "No"
    if len(ctr) == 2:
        for el in ctr:
            if ctr[el] == 1:
                return "No"
        return "Yes"
    if len(ctr) == 3:
        for el in ctr:
            if ctr[el] > 1:
                return "Yes"
    return "No"

print(check(ctr))