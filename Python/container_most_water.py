class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        ans = 0

        while left < right:
            water = min(height[left], height[right]) * (right - left)
            if water > ans:
                ans = water

            # Keep the better side, so if left lower, we move left hoping for a higher pole
            if height[left] < height[right]:
                left += 1

            # If right lower, then we move the right side down hoping for a higher pole
            else:
                right -= 1
        return ans

height = [1,8,6,2,5,4,8,3,7]
height = [1,2,1]
print(maxArea(height))