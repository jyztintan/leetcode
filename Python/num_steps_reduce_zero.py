class Solution:
    def numberOfSteps(self, num: int) -> int:
        num = bin(num)[2:]
        return len(num) + num.count('1') - 1

print(Solution().numberOfSteps(14))
