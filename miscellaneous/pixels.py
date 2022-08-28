from collections import Counter

t = int(input())

for _ in range(t):
    s = input() + input()
    ctr = sorted(Counter(s).values())
    if ctr == [1, 1, 1, 1]:
        print(3)
    elif ctr == [4]:
        print(0)
    elif ctr == [1, 1, 2]:
        print(2)
    elif ctr == [2, 2] or ctr == [1, 3]:
        print(1)