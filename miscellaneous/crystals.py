a, b = map(int, input().split())
x, y, z = map(int, input().split())

violet = 2 * x + y
red = y + 3 * z

print(max(violet - a, 0) + max(red - b, 0))