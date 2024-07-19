class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if len(cost) <= 2:
            return min(cost)

        return min(self.minCostClimbingStairs(cost[1:],) ,  self.minCostClimbingStairs(cost[1:],)

cost = [10,15,20]
print(Solution().minCostClimbingStairs(cost))
cost = [1,100,1,1,1,100,1,1,100,1]
print(Solution().minCostClimbingStairs(cost))
cost = [0, 2, 2, 1]
print(Solution().minCostClimbingStairs(cost))
