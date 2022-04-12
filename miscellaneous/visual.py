null = " "
tree = eval(input())
n = len(tree)

mdigits = max(tree, key = lambda node: len(str(node)))
mdigits = 3
null = " " * mdigits

levels = {}

paths= [(0, 0, 0)]
i = 0

def getHeight(i):
    if i < n:
        return 1 + max(getHeight(2 * i + 1), getHeight(2 * i + 2))
    return 0

h = getHeight(0)
cols = (1 << h) - 1
rows = h
op = [[null for i in range(cols)] for j in range(rows)]
nodes = [(0, 0, 0, cols)]
while len(nodes) > 0:
    curr, l, a, b = nodes.pop()
    if curr < n:
        i = (a + b) // 2
        op[l][i] = ("{:"+ str(mdigits) +"}").format(tree[curr])
        nodes.append((2 * curr + 1, l + 1, a, i))
        nodes.append((2 * curr + 2, l + 1, i, b))

print("\n".join(["".join(row) + "\n" * mdigits for row in op]))
