s = input()

n = len(s)

valid = True

syms = {'A', 'H', 'I', 'M', 'o', 'O', 'T', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'Y'}

for i in range(1 + n // 2):
    if s[i] == s[n - i - 1]:
        if s[i] not in syms:
            valid = False
            break
    else:
        if sorted([s[i], s[n - i - 1]]) != ['b', 'd'] and sorted([s[i], s[n - i - 1]]) != ['p', 'q']:
            valid = False
            break

print("TAK" if valid else "NIE")