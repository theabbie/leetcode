MAX = 100001

ctr = [0] * MAX
s = [0] * MAX

for i in range(1, MAX):
    j = 1
    while i * j < MAX:
        ctr[i * j] += 1
        s[i * j] += i
        j += 1

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(s[el] for el in nums if ctr[el] == 4)