import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital) -> int:
        # Note that capital is not "spent" when taking on the project
        # This is because it is profits array not a revenue array xdxp

        n = len(profits)

        # Store projects as (cost, gain) in a consolidated list
        # By sorting this, we can just keep a pointer to avoid repeated processing
        projects = sorted(zip(capital, profits))

        # Max Heap to get the most profitable projects, at any one time
        max_heap = []

        # Pointer for the projects we have processed in the sorted projects list
        j = 0

        # Take a maximum of k projects
        for _ in range(k):

            # The first condition ensures we don't get an IndexOutOfBounds error
            # The second condition ensures we only add projects we can afford
            while j < n and w >= projects[j][0]:
                # We add this affordable project into the max heap
                # Negate the profit to follow the sorting behaviour of the max heap
                heapq.heappush(max_heap, -projects[j][1])
                j += 1

            # Check that our max_heap is non-empty
            if max_heap:
                # Take on the most profitable project
                best_profit = -heapq.heappop(max_heap)
                # Update our new capital
                w += best_profit
            # If our max_heap is empty, means we can't afford anymore projects :(
            # Terminate early for better time efficiency
            else:
                break

        return w

# sol = Solution()
# profits = [1,2,3]
# capital = [1,1,2]
# print(sol.findMaximizedCapital(1, 2, profits, capital))