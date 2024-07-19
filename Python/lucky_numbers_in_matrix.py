class Solution:
    def luckyNumbers(self, matrix):
        lows = set()
        for row in matrix:
             lows.add(min(row))

        highs = set()
        matrix = zip(*matrix)
        for column in matrix:
            highs.add(max(column))

        return list(highs.intersection(lows))

# matrix = [[3,7,8],[9,11,13],[15,16,17]]
# print(Solution().luckyNumbers(matrix))