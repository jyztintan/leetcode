class Solution:
    def largestRectangleArea(self, heights) -> int:
        st = []
        max_area = 0

        for i, height in enumerate(heights):

            # If this is not a lower height, no issue
            # If this is a lower height, then we need to move the "start" point to where we popped last
            # This is to account for cases where there is a decrease and increase again
            new_start = i

            # If this height is lower than value(s) before
            while st and height < st[-1][1]:

                # Then we pop those as those values can no longer be "extended" to the right
                idx, higher = st.pop()

                # Calculate the max area those heights can reach (this point is the limit)
                popped_area = (i - idx) * higher

                # If the calculated is area is greater than max recorded area, replace it
                max_area = max(max_area, popped_area)

                # We need to move the new "start" point to where we popped the last height
                new_start = idx
            st.append((new_start, height))

        # Account for those heights still in stack
        for idx, higher in st:

            # Check for max_areas
            max_area = max(max_area, higher * (len(heights) - idx))

        return max_area

# sol = Solution()
# heights = [2,1,5,6,2,3]
# print(sol.largestRectangleArea(heights))
# heights = [3,5,1,7,5,9]
# print(sol.largestRectangleArea(heights))
