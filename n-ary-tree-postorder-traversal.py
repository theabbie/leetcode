class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        o = lambda x: [] if not x else sum([o(c) for c in x.children], []) + [x.val]
        return o(root)