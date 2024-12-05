class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add initial dummy value for stack (this will never be popped)
        stack = [[-1, 0]]
        max_area = 0
        # Add dummy final height to resolve those still in stack
        heights.append(0)
        for idx, height in enumerate(heights):
            # Whenever we encounter a descending height, we take all previous possible heights and generate
            # a rectangle with longest possible width
            while stack and stack[-1][0] >= height:
                prev_height, prev_idx = stack.pop()
                width = idx - stack[-1][1]
                max_area = max(max_area, prev_height * width)
            stack.append((height, idx + 1))
        return max_area

# sol = Solution()
# heights = [2,1,5,6,2,3]
# print(sol.largestRectangleArea(heights))
# heights = [3,5,1,7,5,9]
# print(sol.largestRectangleArea(heights))
