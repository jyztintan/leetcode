class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height) - 1
        while l < r:
            l_height, r_height = height[l], height[r]
            ans = max(ans, (r - l) * min(l_height, r_height))

            # We keep the better side, so if left is lower, we shift left up, hoping for a higher pole
            if l_height < r_height:
                l += 1
            else:
                r -= 1

        return ans

# height = [1,8,6,2,5,4,8,3,7]
# height = [1,2,1]
# print(maxArea(height))