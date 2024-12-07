import heapq
# Solution 1: Quick Select
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        lower = len(nums) - k
        def quick_select(left, right):
            idx = (left + right) // 2
            pivot = nums[idx]
            nums[idx], nums[right] = nums[right], nums[idx]
            pointer = left

            # Shift all elements less than pivot to the left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                    pointer += 1
            nums[pointer], nums[right] = nums[right], nums[pointer]

            if pointer > lower:
                return quick_select(left, pointer - 1)
            elif pointer < lower:
                return quick_select(pointer + 1, right)
            else:
                return pivot

        return quick_select(0, len(nums) - 1)

print(Solution().findKthLargest([3,2,1,5,6,4], 2))


# Solution 2: Max Heap
# Classic
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        max_heap = []
        heapq.heapify(max_heap)

        for num in nums:
            heapq.heappush(max_heap, -num)

        for i in range(k - 1):
            heapq.heappop(max_heap)

        return -heapq.heappop(max_heap)

# Elegant one pass
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We keep a min_heap with k elements so the kth largest will always be on the top of the heap
        min_heap = []
        for num in nums:
            if len(min_heap) < k:
                heappush(min_heap, num)
            elif num > min_heap[0]:
                heapreplace(min_heap, num)
        return min_heap[0]