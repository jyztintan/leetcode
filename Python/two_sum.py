class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                return [d[nums[i]], i]
            d[target - nums[i]] = i


# nums = [3,2,4]
# target = 6
# print(twoSum(nums, target))
