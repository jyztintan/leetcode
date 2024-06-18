class Solution:
    def search(self, nums, target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1

# nums = [-1,0,3,5,9,12]
# target = 9
# print(Solution().search(nums, target))
# nums = [-1,0,3,5,9,12]
# target = 2
# print(Solution().search(nums, target))