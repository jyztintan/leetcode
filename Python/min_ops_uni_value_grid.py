class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        remainder = grid[0][0] % x
        elements = []
        for row in grid:
            for ele in row:
                if ele % x != remainder:
                    return -1
                elements.append(ele)

        elements.sort()

        median = elements[len(elements) // 2]
        diff = 0
        for ele in elements:
            diff += abs(ele - median)
        return diff // x
