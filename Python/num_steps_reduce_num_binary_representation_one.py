class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        carry = 0
        for i in range(len(s) - 1, 0, -1):
            digit = int(s[i]) + carry
            if digit % 2 == 1:
                count += 1
                carry = 1
            count += 1
        return count + carry
