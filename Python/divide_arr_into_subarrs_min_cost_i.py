class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        smaller, smallest = inf, inf
        for num in nums[1:]:
            if num < smallest:
                smaller = smallest
                smallest = num
            elif num < smaller:
                smaller = num
        return nums[0] + smaller + smallest
