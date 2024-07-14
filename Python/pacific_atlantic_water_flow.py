import queue


class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])

        pacific = queue.Queue()
        atlantic = queue.Queue()
        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific.put((row, col))
                if row == rows - 1 or col == cols - 1:
                    atlantic.put((row, col))

        pacific_flow = set()
        while not pacific.empty():
            row, col = pacific.get()
            curr = heights[row][col]
            pacific_flow.add((row, col))

            # BFS Downwards
            if row + 1 < rows and curr <= heights[row + 1][col] and (row + 1, col) not in pacific_flow:
                pacific.put((row + 1, col))

            # BFS Right
            if col + 1 < cols and curr <= heights[row][col + 1] and (row, col + 1) not in pacific_flow:
                pacific.put((row, col + 1))

            # BFS Upwards
            if row > 0 and curr <= heights[row - 1][col] and (row - 1, col) not in pacific_flow:
                pacific.put((row - 1, col))

            # BFS Left
            if col > 0 and curr <= heights[row][col - 1] and (row, col - 1) not in pacific_flow:
                pacific.put((row, col - 1))

        atlantic_flow = set()
        while not atlantic.empty():
            row, col = atlantic.get()
            curr = heights[row][col]
            atlantic_flow.add((row, col))

            # BFS Downwards
            if row + 1 < rows and curr <= heights[row + 1][col] and (row + 1, col) not in atlantic_flow:
                atlantic.put((row + 1, col))

            # BFS Right
            if col + 1 < cols and curr <= heights[row][col + 1] and (row, col + 1) not in atlantic_flow:
                atlantic.put((row, col + 1))

            # BFS Upwards
            if row > 0 and curr <= heights[row - 1][col] and (row - 1, col) not in atlantic_flow:
                atlantic.put((row - 1, col))

            # BFS Left
            if col > 0 and curr <= heights[row][col - 1] and (row, col - 1) not in atlantic_flow:
                atlantic.put((row, col - 1))

        return list(atlantic_flow.intersection(pacific_flow))

# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# print(Solution().pacificAtlantic(heights))
# heights = [[0]]
# print(Solution().pacificAtlantic(heights))
# heights = [[1,2,3],[8,9,4],[7,6,5]]
# print(Solution().pacificAtlantic(heights))
