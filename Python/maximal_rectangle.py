class Solution:
    def maximalRectangle(self, matrix) -> int:
        # Keep track of each column value, represented in a histogram format ish
        processed = [0] * len(matrix[0])
        ans = 0
        for row in matrix:
            for i in range(len(row)):

                # Increment the column value by 1 if there is a value
                if row[i] == "1":
                    processed[i] += 1

                # Otherwise the value needs to be reset to 0 as it is not contiguous
                else:
                    processed[i] = 0

            # After every round of processing, check for the greatest area in the new histogram
            ans = max(ans, self.largestRectangleArea(processed))
        return ans

    # This method checks for the maximum area given an array of integers
    # representing the histogram's bar height.
    # See largest_rectangle_histogram.py for more information
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

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalRectangle(matrix))