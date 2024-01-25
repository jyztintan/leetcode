def maxArea(height) -> int:
    ans = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        if area > ans:
            ans = area
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return ans 


height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))