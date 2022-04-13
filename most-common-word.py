from collections import Counter;
import heapq

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        words = []
        paragraph += " ";
        chunk = "";
        for c in paragraph:
            if not c.isalpha():
                if len(chunk) > 0:
                    words.append(chunk)
                    chunk = ""
            else:
                chunk += c.lower()
        ctr = Counter(words)
        heap = [(-v, k) for k, v in ctr.items()]
        heapq.heapify(heap)
        freq = heapq.heappop(heap)[1]
        while freq in banned:
            freq = heapq.heappop(heap)[1]
        return freq