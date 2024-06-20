class Solution:

    def search(self, nums, target: int) -> int:
        def findMin(nums) -> int:
            left, right = 0, len(nums) - 1
            if len(nums) == 1:
                return 0
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < nums[mid - 1]:
                    return mid
                elif nums[mid] < nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            return right

        min_index = findMin(nums)

        def search_inside(nums, target: int) -> int:
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

        if target > nums[-1]:
            return search_inside(nums[:min_index], target)
        else:
            ans = search_inside(nums[min_index:], target)
            if ans != -1:
                ans += min_index
            return ans


nums = [4,5,6,7,0,1,2]
print(Solution().search(nums, 2))
nums = [3, 1]
print(Solution().search(nums, 0))
