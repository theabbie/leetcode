a, b = map(int, input().split())

bb = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

if a in bb[0] and b in bb[0]:
    print("Yes")
elif a in bb[1] and b in bb[1]:
    print("Yes")
elif a in bb[2] and b in bb[2]:
    print("Yes")
else:
    print("No")