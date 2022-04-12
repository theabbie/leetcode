def insert(arr, val):
    beg = 0
    end = len(arr) - 1
    while beg < end:
        mid = (beg + end) // 2
        if arr[mid] >= val:
            beg = mid + 1
        else:
            end = mid
    return beg

print(insert([1, 1], 1))