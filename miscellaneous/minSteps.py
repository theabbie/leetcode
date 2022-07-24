arr = [20, 14, 1, 4, 20]

start, end = 8, 4288

queue = [(start, 0)]
i = 0

while i < len(queue):
    curr, steps = queue[i]
    if curr == end:
        print(steps)
        break
    for el in arr:
        queue.append(((curr * el) % 100000, steps + 1))
    i += 1
