class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        # memo = {len(cost) : 0, len(cost) - 1 : cost[-1]}
        #
        # def min_cost(step):
        #     if step in memo:
        #         return memo[step]
        #     memo[step] = cost[step] + min(min_cost(step + 1), min_cost(step + 2))
        #
        # return min(min_cost(0), min_cost(1))

        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])

# cost = [10,15,20]
# print(Solution().minCostClimbingStairs(cost))
# cost = [1,100,1,1,1,100,1,1,100,1]
# print(Solution().minCostClimbingStairs(cost))
# cost = [0, 2, 2, 1]
# print(Solution().minCostClimbingStairs(cost))
