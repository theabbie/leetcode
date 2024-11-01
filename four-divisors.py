MAX = 10 ** 5
ctr = [0] * (MAX + 1)
s = [0] * (MAX + 1)
for i in range(1, MAX + 1):
    mul = 1
    while i * mul <= MAX:
        ctr[i * mul] += 1
        s[i * mul] += i
        mul += 1
for i in range(MAX + 1):
    if ctr[i] != 4:
        s[i] = 0
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        return sum(s[el] for el in nums)