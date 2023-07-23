n, k = map(int, input().split())

s = list(input())

rem = k

for i in range(n):
    if s[i] == "o":
        if rem > 0:
            rem -= 1
        else:
            s[i] = "x"

print("".join(s))