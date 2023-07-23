t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    chars = set()
    for i in range(n - 1):
        chars.add(s[i:i+2])
    print(len(chars))