class Solution:
    def minSwaps(self, nums) -> int:
        # Total length of array
        n = len(nums)

        # The number of ones in the array that we want to group together
        total = sum(nums)

        # Number of zeros in the current window
        # Note that the number of zeros in the window represent the number of swaps required
        best = curr = nums[:total].count(0)

        # Slide the window
        for left in range(n):
            # Stop accounting for the left-most number
            if not nums[left]:
                curr -= 1
            # Start accounting for the right-most number
            if not nums[(left + total) % n]:
                curr += 1
            # We find the least number of swaps (number of zeros)  among every window
            best = min(best, curr)
        return best


# nums = [0,1,0,1,1,0,0]
# print(Solution().minSwaps(nums))
# nums = [0,1,1,1,0,0,1,1,0]
# print(Solution().minSwaps(nums))
# nums = [1,1,0,0,1]
# print(Solution().minSwaps(nums))
