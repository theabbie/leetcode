s = input()

n = len(s)

def check(s, n):
    prev = None
    for i in range(n):
        if prev == None and i > 0 and s[i] == 'B' and s[i - 1] == 'A':
            prev = i
        if i < n - 1 and s[i] == 'B' and s[i + 1] == 'A' and prev != None and prev < i:
            return "YES"
    prev = None
    for i in range(n):
        if prev == None and i > 0 and s[i] == 'A' and s[i - 1] == 'B':
            prev = i
        if i < n - 1 and s[i] == 'A' and s[i + 1] == 'B' and prev != None and prev < i:
            return "YES"
    return "NO"

print(check(s, n))