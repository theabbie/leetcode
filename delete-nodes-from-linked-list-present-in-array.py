class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        def get(r):
            if not r:
                return r
            if r.val in nums:
                return get(r.next)
            r.next = get(r.next)
            return r
        return get(head)