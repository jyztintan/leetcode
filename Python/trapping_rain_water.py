class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # Create the 2 pointers, and keep track of highest height from left and right
        l, max_left = 0, height[0]
        r = len(height) - 1
        max_right = height[r]
        total = 0

        # While the 2 pointers converge, we always keep the higher one to make sure our ans is optimised
        while l < r:

            # Right is higher than left, so keep the right and move the left up hoping for a higher one
            if max_left < max_right:
                l += 1

                # For this new column, if it is lower than the previous highest, then we add the volume water trapped
                # which is just the difference. Otherwise, it is the new highest and no water trapped.
                # We can be sure the water is trapped since the right highest is guaranteed to be higher than left
                total += max(0, (max_left - height[l]))
                max_left = max(max_left, height[l])

            # Left higher than right, so keep the left and move right down hoping for a higher one
            else:
                r -= 1

                # For this new column, if it is lower than the previous highest, then we add the volume water trapped
                # which is just the difference. Otherwise, it is the new highest and no water trapped.
                # We can be sure the water is trapped since the left highest is guaranteed to be higher than right
                total += max(0, max_right - height[r])
                max_right = max(max_right, height[r])
        return total


# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(height))
# height = [4,2,0,3,2,5]
# print(trap(height))
