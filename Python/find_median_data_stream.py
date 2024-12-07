from heapq import *


class MedianFinder:

    def __init__(self):
        # Store upper half
        self.min_heap = []

        # Store lower half values
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heappush(self.min_heap, num)
            return

        if num >= self.min_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, - num)

        # The max heap must be smaller than the min heap
        # The min heap can at most be 1 element bigger than the max heap
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, - heappop(self.min_heap))
        elif len(self.min_heap) < len(self.max_heap):
            heappush(self.min_heap, - heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        middle1 = - self.max_heap[0]
        middle2 = self.min_heap[0]
        return (middle1 + middle2) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
class MedianFinder:

    def __init__(self):

        # Max Heap for lower half values
        self.lower = []
        heapq.heapify(self.lower)

        # Min Heap for upper half values
        self.upper = []
        heapq.heapify(self.upper)

    def addNum(self, num: int) -> None:

        # If its the first value, put in lower half since we allow it to be longer than the upper half of length 1
        if not self.lower:
            heapq.heappush(self.lower, -num)
            return

        # Current low_mid value
        low_mid = -self.lower[0]

        # If the new num is less than the low_mid, this new num belongs in the lower half
        if num < low_mid:
            heapq.heappush(self.lower, -num)

            # If the length of lower half exceeds length of upper half by more than 1,
            # We pop the highest value of the lower half (which is low_mid) and push it to the upper half
            if len(self.lower) - len(self.upper) > 1:
                heapq.heappush(self.upper, -heapq.heappop(self.lower))

        # If the new num > than the low_mid, this new num belongs in the upper half
        else:
            heapq.heappush(self.upper, num)

            # The length of upper half should never exceed length of lower half,
            # We pop the lowest value of the upper half and push it to the lower half
            if len(self.upper) > len(self.lower):
                heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        # If there are an odd length of numbers in this data structure,
        # We just return the highest value in the lower half, as that will be the median
        if len(self.lower) > len(self.upper):
            return - self.lower[0]
        # Otherwise, we calculate the mean of the 2 middle values
        # Which are the highest value in the lower half and the lowest value in the upper half
        else:
            return (self.upper[0] - self.lower[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(2)
# obj.addNum(1)
# print(obj.findMedian())
# obj.addNum(3)
# print(obj.findMedian())
