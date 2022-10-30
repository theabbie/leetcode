def MEX(arr):
    arr.sort()
    p = [0]
    for el in arr:
        p.append(p[-1] + el)
    return p

print(MEX([0,1,3,4]))