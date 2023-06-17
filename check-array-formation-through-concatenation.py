class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        pos = {}
        for i, el in enumerate(arr):
            pos[el] = i
        joined = []
        for piece in sorted(pieces, key = lambda piece: [pos.get(el, -1) for el in piece]):
            joined.extend(piece)
        return arr == joined