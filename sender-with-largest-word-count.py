from collections import Counter

class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        n = len(senders)
        ctr = Counter()
        for i in range(n):
            ctr[senders[i]] += len(messages[i].split())
        return max(senders, key = lambda sender: (ctr[sender], sender))