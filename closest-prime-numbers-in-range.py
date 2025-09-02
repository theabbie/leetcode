class Solution:
    def segmented_sieve(self, left, right):
        if left < 2:
            left = 2
        
        limit = int(math.sqrt(right)) + 1
        is_prime_small = [True] * (limit + 1)
        is_prime = [True] * (right - left + 1)
        
        for num in range(2, limit + 1):
            if is_prime_small[num]:
                for multiple in range(num * num, limit + 1, num):
                    is_prime_small[multiple] = False
                for multiple in range(max(num * num, (left + num - 1) // num * num), right + 1, num):
                    is_prime[multiple - left] = False
        
        return [num for num, prime in enumerate(is_prime, start=left) if prime]

    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.segmented_sieve(left, right)
        if len(primes) < 2:
            return [-1, -1]
        return min((primes[i+1] - primes[i], (primes[i], primes[i + 1])) for i in range(len(primes) - 1))[1]