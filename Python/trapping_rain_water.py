class Solution:
    def trap(self, height: List[int]) -> int:
        collected = 0
        left, right = 0, len(height) - 1
        left_highest, right_highest = height[left], height[right]
        while left < right:
            if height[left] < height[right]:
                left += 1
                left_highest = max(height[left], left_highest)
                collected += left_highest - height[left]
            else:
                right -= 1
                right_highest = max(height[right], right_highest)
                collected += right_highest - height[right]
        return collected


# Brute force solution O(N^2) because we find the minimum of the left and right maximum pillars for each bar
class Solution:
    def trap(self, height: List[int]) -> int:
        collected = 0
        n = len(height)
        for mid in range(1, n - 1):
            left_max = 0
            for l in range(mid, -1, -1):
                left_max = max(left_max, height[l])
            right_max = 0
            for r in range(mid, n):
                right_max = max(right_max, height[r])
            collected += min(left_max, right_max) - height[mid]
        return collected



# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# print(trap(height))
# height = [4,2,0,3,2,5]
# print(trap(height))
