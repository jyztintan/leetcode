# Time: O(N*k) for finding the smallest number and modifying it k times
# Space: O(1) No additional space needed as we are modifying the array in-place
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for _ in range(k):
            smallest = min(nums)
            idx = nums.index(smallest)
            nums[idx] *= multiplier

        return nums

# Time: O(NlogN + klogN) for creating the min_heap and for k * heappop/push processes
# Space: O(N) for storing the min_heap
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for idx, num in enumerate(nums):
            heappush(min_heap, (num, idx))

        for _ in range(k):
            num, idx = heappop(min_heap)
            heappush(min_heap, (num * multiplier, idx))

        for num, idx in min_heap:
            nums[idx] = num

        return nums
