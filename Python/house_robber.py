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


