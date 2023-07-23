n = int(input())

arr = []

for _ in range(n):
    arr.append(input())

def check(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            s = arr[i] + arr[j]
            if s == s[::-1]:
                return True
    return False

print("Yes" if check(arr) else "No")