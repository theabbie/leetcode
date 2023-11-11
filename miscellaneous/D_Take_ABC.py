s = input()

stack = []

for c in s:
    delt = False
    if len(stack) >= 2 and stack[-2] + stack[-1] + c == "ABC":
        stack.pop()
        stack.pop()
    else:
        stack.append(c)

print("".join(stack))