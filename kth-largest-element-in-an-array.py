class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q=lambda a,k:a[0]if len(a)==1 else (lambda L,M,R:q(L,k)if k<len(L)else M[0]if k<len(L)+len(M)else q(R,k-len(L)-len(M)))([x for x in a if x<a[len(a)//2]],[x for x in a if x==a[len(a)//2]],[x for x in a if x>a[len(a)//2]])
        return q(nums,len(nums)-k)