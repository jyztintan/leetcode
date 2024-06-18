class Solution:
    def findMin(self, nums) -> int:
        left, right = 0, len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[right]


# nums = [3,4,5,1,2]
# print(Solution().findMin(nums))
# nums = [4,5,6,7,0,1,2]
# print(Solution().findMin(nums))
# nums = [11, 13, 15, 17]
# print(Solution().findMin(nums))
