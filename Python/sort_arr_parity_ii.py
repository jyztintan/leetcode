# Time: O(N)
# Space: O(1) in-place sorting
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        while even < len(nums):
            if nums[even] % 2 != 0:
                while nums[odd] % 2 == 1:
                    odd += 2
                nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
        return nums
