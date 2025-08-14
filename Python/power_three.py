# O(1) Solution -> 3 is a prime number so the maximum 3 ** x number should only be divisible by 3 and other 3 ** x
# Also note that all 3 ** x > 0
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0

# O(log_3(n) Solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        curr = 0
        while 3 ** curr < n:
            curr += 1
        return 3 ** curr == n
