import heapq


class Solution:
    def minOperations(self, nums, k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while nums[0] < k:
            x, y = heapq.heappop(nums), heapq.heappop(nums)
            num = x * 2 + y
            heapq.heappush(nums, num)
            count += 1
        return count
