class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        n = len(vals)
        rem = [False] * n
        mval = float('-inf')
        for i in range(n - 1, -1, -1):
            if vals[i] < mval:
                rem[i] = True
            mval = max(mval, vals[i])
        nodes = []
        curr = head
        i = 0
        while curr:
            if not rem[i]:
                nodes.append(curr)
            curr = curr.next
            i += 1
        n = len(nodes)
        for i in range(n - 1):
            nodes[i].next = nodes[i + 1]
        return nodes[0]