class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = {}

        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            best = 1
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n and matrix[new_row][new_col] > matrix[row][col]:
                    best = max(best, dfs(new_row, new_col) + 1)
            memo[(row, col)] = best
            return best

        best = 0
        for row in range(m):
            for col in range(n):
                best = max(best, dfs(row, col))
        return best


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        # We can map each number to an index number in the matrix
        # And represent the relation in which a number is less than another as an edge
        # Then this becomes a longest path graph problem :)
        m, n = len(matrix), len(matrix[0])
        adj_list = {}

        def get_adjacent(row, col):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            lst = []
            for x, y in directions:
                if x + row < 0 or x + row >= m or y + col < 0 or y + col >= n:
                    continue
                if matrix[row][col] < matrix[row + x][col + y]:
                    lst.append((x + row) * n + y + col)
            return lst


        for i in range(m):
            for j in range(n):
                adj_list[i * n + j] = get_adjacent(i, j)

        # Now that we have a robust adjacency list, all we need to do is get the longest path in this graph
        visited = [0] * (m * n)
        def dfs(start):
            if visited[start]:
                return visited[start]
            if not adj_list[start]:
                visited[start] = 1
                return 1
            longest = -1
            for neighbour in adj_list[start]:
                longest = max(longest, dfs(neighbour) + 1)
            visited[start] = longest
            return longest

        for i in range(m * n):
            dfs(i)

        return max(visited)

# matrix = [[0],[1],[5],[5]]
# print(Solution().longestIncreasingPath(matrix))
