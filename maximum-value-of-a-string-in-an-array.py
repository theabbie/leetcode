class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def val(x):
            try:
                return int(x)
            except:
                return len(x)
        return max([val(s) for s in strs])