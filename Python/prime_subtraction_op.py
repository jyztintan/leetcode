from bisect import bisect_left


class Solution:
    def primeSubOperation(self, nums) -> bool:
        max_num = max(nums)
        is_prime = [True] * (max_num + 1)
        is_prime[0] = is_prime[1] = False
        # Sieve of Eratosthenes wow
        for i in range(2, int(max_num ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num + 1, i):
                    is_prime[j] = False

        primes = [i for i, prime in enumerate(is_prime) if prime]

        prev = 0
        for num in nums:
            if num <= prev:
                return False
            j = bisect_left(primes, num - prev) - 1
            if j != -1:
                num -= primes[j]
            prev = num

        return True


print(Solution().primeSubOperation([4,9,6,10]))