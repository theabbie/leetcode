class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        for word in strs:
            key = "".join(sorted(word))
            buckets[key] = buckets.get(key, []) + [word]
        return list(buckets.values())