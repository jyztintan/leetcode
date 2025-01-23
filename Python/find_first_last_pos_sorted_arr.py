class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1

        # Find smallest index
        smallest = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                smallest = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        if smallest == -1:
            return [-1, -1]

        # Find largest index
        left, right = 0, len(nums) - 1
        largest = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                largest = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [smallest, largest]
