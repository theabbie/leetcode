s = input()

print("".join("0" if c == "1" else "1" for c in s))