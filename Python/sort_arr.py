# Counting Sort - Time: O(N), Space: O(N)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lowest = min(nums)
        highest = max(nums)
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        ans = []
        for num in range(lowest, highest + 1):
            for _ in range(freq.get(num, 0)):
                ans.append(num)
        return ans

# Using offset
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        lowest = min(nums)
        highest = max(nums)
        freq = [0] * (highest - lowest + 1)
        for num in nums:
            freq[num - lowest] += 1

        ans = []
        for num in range(lowest, highest + 1):
            for _ in range(freq[num - lowest]):
                ans.append(num)
        return ans

# Quick Sort - Amortised Time: O(NlogN), Space: O(N) for recursive call stack
# Note that quick sort fails for this problem due to edge cases: homogeneous array, sorted array
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(arr, low, high):
            if low >= high:
                return
            pivot_idx = partition(arr, low, high)
            quicksort(arr, low, pivot_idx - 1)
            quicksort(arr, pivot_idx + 1, high)

        def partition(arr, low, high):
            pivot_idx = randint(low, high)
            pivot = arr[pivot_idx]
            arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
            i = low
            for j in range(low, high):
                if arr[j] < pivot:
                    arr[j], arr[i] = arr[i], arr[j]
                    i += 1

            arr[i], arr[high] = arr[high], arr[i]
            return i

        quicksort(nums, 0, len(nums) - 1)
        return nums
