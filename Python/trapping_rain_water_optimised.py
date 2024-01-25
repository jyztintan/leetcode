def trap(height) -> int:
    l, max_left = 0, height[0]
    r = len(height) - 1
    max_right =  height[r]
    total = 0
    while l < r:
        if max_left < max_right:
            l += 1
            if max_left - height[l] > 0:
                total += max_left - height[l]
            max_left = max(max_left, height[l])
        else:
            r -= 1
            if max_right - height[r] > 0:
                total += max_right - height[r]
            max_right = max(max_right, height[r])
    return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
height = [4,2,0,3,2,5]
print(trap(height))