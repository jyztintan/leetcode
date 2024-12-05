class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # Find pivot first
        left, right = 1, n - 1
        pivot = 0
        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                pivot = mid
                break
            elif nums[mid] > nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        shift = n - pivot
        left, right = (pivot + shift) % n, (pivot - 1 + shift) % n

        while left <= right:
            mid = (left + right) // 2
            if nums[(mid - shift) % n] == target:
                return (mid - shift) % n
            elif nums[(mid - shift) % n] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
