class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointer = 0

        # Count the number of non-zeros
        for i in range(len(nums)):
            if nums[i]:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1

        return nums
