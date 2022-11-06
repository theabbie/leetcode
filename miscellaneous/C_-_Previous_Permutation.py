n = int(input())

arr = list(map(int, input().split()))

def prevPermutation(arr):
    n = len(arr) - 1
    i = n
    while i > 0 and arr[i - 1] <= arr[i]:
        i -= 1
    j = i - 1
    while j + 1 <= n and arr[j + 1] < arr[i - 1]:
        j += 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    arr[i:] = arr[i:][::-1]
    return arr

print(*prevPermutation(arr))