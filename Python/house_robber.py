class Solution:
    def rob(self, nums) -> int:
        if len(nums) < 3:
            return max(nums)

        # Add zeros to buffer for the last 2 houses during our iteration
        nums.append(0)
        nums.append(0)
        nums.append(0)
        for i in range(len(nums) - 4, -1, -1):
            # At each house, we can either go to the house 2 or 3 blocks down.
            # Going to the direct next house violates the rule, going to houses more than 3 blocks down is suboptimal
            # We iterate backwards, accumulating the max possible robberies starting from the ith index house
            nums[i] += max(nums[i + 2], nums[i + 3])

        return max(nums[0], nums[1])


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)

        # We make nums keep track of the highest possible robbing value up to house i
        nums[1] = max(nums[0], nums[1])
        for i in range(2, n):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])

        return max(nums[n - 1], nums[n - 2])

