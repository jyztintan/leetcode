class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        low, high = 0, max(workerTimes) * mountainHeight * mountainHeight

        ans = inf
        while low <= high:
            mid = (low + high) // 2
            count = 0
            for time in workerTimes:
                work = mid // time
                k = int((-1 + ((1 + work * 8) ** 0.5)) / 2)
                count += k
            if count >= mountainHeight:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

# Heap Solution. Time Complexity: O(N + MlogN), where M is the height and N is the number of workers
class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        time = 0
        workers = [(time, time, 2) for time in workerTimes]
        heapify(workers)
        while mountainHeight:
            time, incr, repeat = heappop(workers)
            mountainHeight -= 1
            heappush(workers, (time + incr * repeat, incr, repeat + 1))
        return time
