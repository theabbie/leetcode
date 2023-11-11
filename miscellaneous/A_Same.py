n = int(input())

arr = list(map(int, input().split()))

same = True

for el in arr:
    if el != arr[0]:
        same = False
        break

print("Yes" if same else "No")