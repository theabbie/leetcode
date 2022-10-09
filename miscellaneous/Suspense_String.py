t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    t = ""
    i = 0
    j = n - 1
    alice = True
    while i <= j:
        if alice:
            if s[i] + t <= t + s[i]:
                t = s[i] + t
            else:
                t += s[i]
            i += 1
        else:
            if s[j] + t >= t + s[j]:
                t = s[j] + t
            else:
                t += s[j]
            j -= 1
        alice = not alice
    print(t)