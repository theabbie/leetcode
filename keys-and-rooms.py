class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        beg = 0
        paths = [beg]
        visited = {beg}
        while len(paths) > 0:
            curr = paths.pop()
            for j in rooms[curr]:
                if j not in visited:
                    visited.add(j)
                    paths.append(j)
        return len(visited) == len(rooms)