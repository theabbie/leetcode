t = int(input())

def solve(arr):
    arr.sort(reverse = True)
    xor = 0
    for el in arr:
        xor ^= el
        if xor != 0:
            return "Marichka"
    return "Zenyk"

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(solve(arr))