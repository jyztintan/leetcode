class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        max_or = 0
        for num in nums:
            max_or |= num

        count = 0
        n = len(nums)
        subsets = 2 ** n
        for left in range(subsets):
            curr = 0
            for i in range(n):
                if (left // i) & 1:
                    curr |= nums[i]

            if curr == max_or:
                count += 1

        return count

class Solution:
    def countMaxOrSubsets(self, nums) -> int:
        max_or = 0

        dp = [0] * (2 ** 17)
        dp[0] = 1

        for num in nums:
            for i in range(max_or, -1, -1):
                dp[i | num] += dp[i]
            max_or |= num

        return dp[max_or]


nums = [3, 1]
print(Solution().countMaxOrSubsets(nums))
nums = [3,1]
print(Solution().countMaxOrSubsets(nums))