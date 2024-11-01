class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        trie = Node()
        for path in folder:
            curr = trie
            for c in path.split("/"):
                if c not in curr.children:
                    curr.children[c] = Node()
                curr = curr.children[c]
            curr.end = True
        res = []
        def dfs(curr, path):
            if curr.end:
                res.append(path)
                return
            for c in curr.children:
                dfs(curr.children[c], path + ("/" if curr != trie else "") + c)
        dfs(trie, "")
        return res