import heapq
class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.nums = []
        temp = []
        heapq.heapify(temp)
        heapq.heapify(self.nums)
        for num in nums:
            heapq.heappush(temp, -num)
        for i in range(min(k, len(nums))):
            heapq.heappush(self.nums, - heapq.heappop(temp))

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]

test = KthLargest(1, [])
print(test.add(-3))
print(test.add(-2))
print(test.add(-4))
print(test.add(9))
# print(test.add(4))

