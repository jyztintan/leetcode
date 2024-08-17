class Solution:
    def maxPoints(self, points) -> int:
        n = len(points[0])
        prev = [0] * n
        for row in points:
            best = [0] * n

            left_best = [0] * n
            left_best[0] = prev[0]
            right_best = [0] * n
            right_best[n - 1] = prev[n - 1]
            for i in range(1, n):
                left_best[i] = max(left_best[i - 1] - 1, prev[i])
                right_best[n - 1 - i] = max(right_best[n - i] - 1, prev[n - 1 - i])

            for col in range(n):
                best[col] = row[col] + max(left_best[col], right_best[col])

            prev = best
        return max(prev)

points = [[1,5],[2,3],[4,2]]
print(Solution().maxPoints(points))

