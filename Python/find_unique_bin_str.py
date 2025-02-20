# We can speed things up since there is strictly N inputs in num, we can employ Cantor's Diagonalisation LFGGG
# This takes O(N) time since we go through each N inputs and take the complement of the i-th index
# Discrete mathematics is fucking amazing
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        final = []
        for idx, num in enumerate(nums):
            if num[idx] == '0':
                final.append('1')
            else:
                final.append('0')
        return "".join(final)


# Seems inefficient because time complexity is O(2 ** N), where N is the length of the string
# The worst case is when all bin strings from 0 to 2 ** N - 2 is present -> leaving 2 ** N - 1
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        seen = set(nums)
        curr = 0
        while True:
            binary = bin(curr)[2:]
            # Extend leading 0s so that it has n digits
            binary = '0' * (n - len(binary)) + binary
            if binary not in seen:
                return binary
            curr += 1
