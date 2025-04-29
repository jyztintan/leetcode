class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_ele = max(nums)
        n = len(nums)
        left = 0
        count = 0
        max_ele_count = 0

        for right in range(n):
            if nums[right] == max_ele:
                max_ele_count += 1

            while max_ele_count >= k:
                if nums[left] == max_ele:
                    max_ele_count -= 1
                left += 1

            count += left
        return count
