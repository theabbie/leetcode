arr = list(map(int, input().split()))

def check(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return "No"
    for el in arr:
        if not 100 <= el <= 675:
            return "No"
        if el % 25 != 0:
            return "No"
    return "Yes"

print(check(arr))