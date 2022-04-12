# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        total = 0
        for _ in range(10):
            total += rand7()
        return 1 + total % 10
        