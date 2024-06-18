class Solution:
    def largestRectangleArea(self, heights) -> int:
        st = []
        max_area = 0

        for i, height in enumerate(heights):
            new_start = i
            while st and height < st[-1][1]:
                idx, higher = st.pop()
                popped_area = (i - idx) * higher
                max_area = max(max_area, popped_area)
                new_start = idx
            st.append((new_start, height))

        for idx, higher in st:
            max_area = max(max_area, higher * (len(heights) - idx))

        return max_area

# sol = Solution()
# heights = [2,1,5,6,2,3]
# print(sol.largestRectangleArea(heights))
# heights = [3,5,1,7,5,9]
# print(sol.largestRectangleArea(heights))
