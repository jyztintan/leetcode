class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) <= 3:
            return max(nums)

        robbed_first = [0] * n
        skipped_first = [0] * n

        robbed_first[0] = nums[0]
        robbed_first[1] = nums[0]
        for idx in range(2, n - 1):
            robbed_first[idx] = max(robbed_first[idx - 1], robbed_first[idx - 2] + nums[idx])

        skipped_first[1] = nums[1]
        for idx in range(2, n):
            skipped_first[idx] = max(skipped_first[idx - 1], skipped_first[idx - 2] + nums[idx])

        return max(robbed_first[n - 2], skipped_first[n - 1])

class Solution:
    def rob(self, nums) -> int:

        if len(nums) < 3:
            return max(nums)
        def helper(nums):
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

        # We either rob the first and the 2nd last house, or the second and the last house
        return max(helper(nums[:-1]), helper(nums[1:]))

