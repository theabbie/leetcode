from collections import defaultdict, deque

def shortestpath(routes, S, T):
    to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for j in route:
            to_routes[j].add(i)
    bfs = [(S, -1)]
    seen = set([S])
    for stop, bus in bfs:
        if stop == T: return bus
        for i in to_routes[stop]:
            for j in routes[i]:
                if j not in seen:
                    bfs.append((j, bus + 1))
                    seen.add(j)
            routes[i] = []
    return -1

n, m = map(int, input().split())

routes = []

for _ in range(n):
    k = int(input())
    routes.append(list(map(int, input().split())))

print(shortestpath(routes, 1, m))