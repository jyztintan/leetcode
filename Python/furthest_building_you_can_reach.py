class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        def reach_building(idx):
            increments = []
            for building in range(idx):
                if heights[building] < heights[building + 1]:
                    heappush(increments, - (heights[building + 1] - heights[building]))

            for _ in range(ladders):
                if not increments:
                    return True
                heappop(increments)

            return - sum(increments) <= bricks

        low, high = 0, len(heights) - 1
        best = 0

        while low <= high:
            mid = (low + high) // 2
            if reach_building(mid):
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best
