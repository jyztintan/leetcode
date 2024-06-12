class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Keep track of the index start for each colour
        red, white, blue = 0, 0, 0

        # Iterate through the nums list
        for i in range(len(nums)):

            # If colour is red, we need to swap it with the front of the red
            if nums[i] == 0:
                nums[red], nums[i] = nums[i], nums[red]

                # If it so happens we swapped red with a white, then we need to swap white to front of white also
                if nums[i] == 1:
                    nums[white], nums[i] = nums[i], nums[white]

                # Increment indices for all 3 colours since red has the highest priority
                red += 1
                white += 1
                blue += 1

            # If colour is white, we need to swap white to front of white
            elif nums[i] == 1:
                nums[white], nums[i] = nums[i], nums[white]

                # Increment indices for white and blue since white has higher priority over blue
                white += 1
                blue += 1

            # If colour is blue, no swap needed since blues are supposed to be at the end
            else:

                # Increment blue index
                blue += 1
        return nums

sol = Solution()
nums = [2,0,2,1,1,0,0]
print(sol.sortColors(nums))