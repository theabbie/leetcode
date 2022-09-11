class Solution:
    def tree2str(self, root):
        if root:
            l = self.tree2str(root.left)
            r = self.tree2str(root.right)
            lstr = f"({l})" if l or r else ""
            rstr = f"({r})" if r else ""
            return f"{root.val}{lstr}{rstr}"
        return ""