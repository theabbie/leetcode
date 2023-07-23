n = int(input())

s = input()

stack = [("", 0)]

for c in s:
    if c == '(' or c == ')':
        if c == '(':
            stack.append((c, stack[-1][1] + 1))
        else:
            ch = stack[-1][1]
            if ch == 0:
                stack.append((')', stack[-1][1]))
            else:
                while len(stack) > 1 and stack[-1][1] == ch:
                    stack.pop()
    else:
        stack.append((c, stack[-1][1]))

print("".join(el[0] for el in stack))