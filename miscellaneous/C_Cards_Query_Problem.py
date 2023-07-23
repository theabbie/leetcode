from collections import defaultdict

n = int(input())

q = int(input())

boxes = defaultdict(list)
cards = defaultdict(set)

for _ in range(q):
    curr = list(map(int, input().split()))
    if curr[0] == 1:
        cards[curr[1]].add(curr[2])
        boxes[curr[2]].append(curr[1])
    if curr[0] == 2:
        print(*sorted(boxes[curr[1]]))
    if curr[0] == 3:
        print(*sorted(cards[curr[1]]))