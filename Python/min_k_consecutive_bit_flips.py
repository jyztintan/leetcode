class Solution:
    def minKBitFlips(self, nums, k: int) -> int:

        # Number of elements in nums array
        n = len(nums)

        # Keep track of number of flips, and scale which represents the flipping effect
        # Also, an additional array that keeps track of when the flip effect should 'stop'
        flips = scale = 0
        effect = [0] * (n+1)

        # As we iterate through the elements in the array
        for pointer in range(n):

            # Update the flipping effect, for example, if flipping stops then scale will revert back to 0
            scale += effect[pointer]

            # Then our current element that we are processing takes into account any flip effects as well
            # This may include double flipping so we mod it by 2
            curr = (nums[pointer] + scale)%2

            # If the processed element is 0, then we need to initiate a new flip
            if curr == 0:

                # However, if the "end-flip" exceeds the nums array, then we cannot flip k consecutive bits
                # Hence, we are unable to find a valid flipping sequence
                if pointer + k > n:
                    return -1

                # We set the ending index of the flip to -1 so that it will decrement the scale appropriately
                effect[pointer + k] -= 1

                # The flip effect is activated
                scale += 1

                # The number of flips is incremented
                flips += 1

        return flips

# nums = [0,1,0]
# print(Solution().minKBitFlips(nums, 1))
# nums = [1,1,0]
# print(Solution().minKBitFlips(nums, 2))
# nums = [0,0,0,1,0,1,1,0]
# print(Solution().minKBitFlips(nums, 3))