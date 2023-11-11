t = int(input())

for _ in range(t):
    s = list(input())
    s = ["0"] + s
    n = len(s)
    done = False
    for i in range(n):
        if done:
            s[i] = "0"
            continue
        if i < n - 1 and int(s[i + 1]) >= 5:
            s[i] = str(int(s[i]) + 1)
            j = i
            while j > 0 and int(s[j]) >= 5: 
                s[j] = "0"
                s[j - 1] = str(int(s[j - 1]) + 1)
                j -= 1
            done = True
    if s[0] == "0":
        s.pop(0)
    print("".join(s))