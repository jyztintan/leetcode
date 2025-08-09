# O(1)
# The power of 2 is the number with binary regex form: 1(0)*
# Hence, there should be no common bit with its predecessor;
# All numbers not power of 2 will have the most significant bit as a common bit
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0

# O(logN)
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        while n >= 2:
            if n == 2:
                return True
            n /= 2
        return False
