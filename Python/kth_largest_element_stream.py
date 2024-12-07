from heapq import *


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.capacity = k

        # Only extract out the top k elements
        temp = []
        for num in nums:
            heappush(temp, - num)

        # The kth element will be on the top of the min_heap
        self.min_heap = []
        for _ in range(min(k, len(nums))):
            heappush(self.min_heap, - heappop(temp))

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.capacity:
            heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapreplace(self.min_heap, val)
        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)