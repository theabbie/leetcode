class Solution:
    def getDirections(self, root, startValue, destValue) -> str:
        if not root:
            return ""
        graph = defaultdict(set)
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.left:
                graph[curr.val].add((curr.left.val, "L"))
                graph[curr.left.val].add((curr.val, "U"))
                stack.append(curr.left)
            if curr.right:
                graph[curr.val].add((curr.right.val, "R"))
                graph[curr.right.val].add((curr.val, "U"))
                stack.append(curr.right)
        q = deque([startValue])
        v = {startValue}
        prev = {}
        while q:
            x = q.pop()
            for y, d in graph[x]:
                if y not in v:
                    prev[y] = (x, d)
                    v.add(y)
                    q.appendleft(y)
        res = [(destValue, "")]
        while res[-1][0] != startValue:
            res.append(prev[res[-1][0]])
        res.reverse()
        return "".join(x[1] for x in res)