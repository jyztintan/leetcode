class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Sieve of Eratosthenes
        primes = [True] * (right + 1)
        primes[0] = primes[1] = False

        for num in range(2, int(sqrt(right)) + 1):
            if primes[num]:
                for mult in range(num * num, right + 1, num):
                    primes[mult] = False

        relevant_primes = [num for num in range(left, right + 1) if primes[num]]

        # Get min diff
        if len(relevant_primes) < 2:
            return -1, -1

        diff = float('inf')
        idx = 0

        for ptr in range(len(relevant_primes) - 1):
            curr = relevant_primes[ptr + 1] - relevant_primes[ptr]
            if curr < diff:
                diff = curr
                idx = ptr
        return relevant_primes[idx], relevant_primes[idx + 1]
