class Solution:
    def isSubPath(self, head, root):
        def check(r, h, f):
            if not h:
                return True
            if not r:
                return False
            if f and (check(r.left, h, f) or check(r.right, h, f)):
                return True
            if h.val != r.val:
                return False
            return check(r.left, h.next, False) or check(r.right, h.next, False)
        return check(root, head, True)