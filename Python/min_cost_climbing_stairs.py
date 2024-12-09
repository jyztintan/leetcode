class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        for i in range(2, len(cost) + 1):
            cost[i] += min(cost[i - 1], cost[i - 2])

        return cost[n - 1]

class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])

        return min(cost[0], cost[1])
