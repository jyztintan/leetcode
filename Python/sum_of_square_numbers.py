import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        limit = math.ceil(math.sqrt(c))
        left, right = 0, limit
        while left <= right:
            ans = left ** 2 + right ** 2
            if ans == c:
                return True
            if ans > c:
                right -= 1
            elif ans < c:
                left += 1
        return False

# solution = Solution()
# print(solution.judgeSquareSum(5))
# print(solution.judgeSquareSum(3))
# print(solution.judgeSquareSum(2))
