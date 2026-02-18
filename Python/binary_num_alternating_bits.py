class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        binary = bin(n)[2:]
        prev = '0'
        for bit in binary:
            if bit == prev:
                return False
            prev = bit
        return True
