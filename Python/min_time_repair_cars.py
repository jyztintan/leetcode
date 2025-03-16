# Binary Search solution
# Time Complexity: O(Rlog(min(R) * C * C))
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        low, high = 0, min(ranks) * cars * cars
        while low < high:
            mid = (low + high) // 2

            # Get the number of cars that can be fixed by each rank
            # within this given amt of time
            cars_built = 0
            for rank in ranks:
                cars_built += int(sqrt(mid // rank))

            if cars_built >= cars:
                high = mid
            else:
                low = mid + 1
        return low

# Heap solution
# O((R + N)log(R)) for time complexity
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        min_heap = []
        for rank in ranks:
            # time, rank, num_cars
            heappush(min_heap, (rank, rank, 1))

        best_time = 0
        for i in range(cars):
            time, rank, num_cars = heappop(min_heap)
            best_time = time
            heappush(min_heap, (rank * (num_cars + 1) * (num_cars + 1), rank, num_cars + 1))
        return best_time
