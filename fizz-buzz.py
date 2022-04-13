class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return [[str(i), "Fizz", "Buzz", "FizzBuzz"][2 * int(i % 5 == 0) + int(i % 3 == 0)] for i in range(1, n + 1)]