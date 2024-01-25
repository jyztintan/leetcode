def trap(heights) -> int:
    max_left = []
    max_right = []
    highest_left = 0
    for num in heights:
        max_left.append(highest_left)
        if num > highest_left:
            highest_left = num
    highest_right = 0
    for num in reversed(heights):
        max_right.append(highest_right)
        if num > highest_right:
            highest_right = num
    max_right.reverse()
    total = 0
    for i in range(len(heights)):
        if height[i] < min(max_left[i], max_right[i]):
            total += min(max_left[i], max_right[i]) - height[i]
    return total


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
height = [4,2,0,3,2,5]
print(trap(height))