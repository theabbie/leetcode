t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    print(max([ord(c) - ord('a') + 1 for c in s]))