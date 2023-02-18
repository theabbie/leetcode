class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        pos = {}
        i = 0
        curr = head
        while curr:
            pos[curr.val] = i
            curr = curr.next
            i += 1
        res = 0
        prev = float('-inf')
        nums.sort(key = lambda el: pos[el])
        for el in nums:
            if pos[el] > prev + 1:
                res += 1
            prev = pos[el]
        return res