def booth_algorithm(string):
    string = string + string  # Duplicate the string to avoid modulo operation
    n = len(string)
    i = 0
    j = 1
    k = 0
    while i < n and j < n and k < n:
        diff = ord(string[(i + k) % n]) - ord(string[(j + k) % n])
        if diff == 0:
            k += 1
        else:
            if diff > 0:
                i = i + k + 1
            else:
                j = j + k + 1
            if i == j:
                j += 1
            k = 0
    rotation_index = min(i, j)
    return string[rotation_index:rotation_index + n//2]

class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        else:
            return booth_algorithm(s)