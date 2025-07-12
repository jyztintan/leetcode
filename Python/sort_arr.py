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

# The problem states to solve the problem without built-in functions in O(nlog(n)) time complexity
# which narrows the sorting algorithms to merge sort, quick sort and heap sort.
# Of which, heap sort is in-place and requires O(1) space. So we choose to implement heap sort.

class Solution:
    def sortArray(self, nums):

        def build_heap(nums):
            non_leaf_index = (len(nums) - 2) // 2
            for i in range(non_leaf_index, -1, -1):
                shift_down(i, nums, len(nums))
            return

        # Compare with children and swap with the smallest child if needed
        def shift_down(curr, nums, last):
            left_child_idx = curr * 2 + 1
            right_child_idx = left_child_idx + 1
            largest_idx = curr

            # If there is only a left child, which happens to be larger than the current node, we swap them
            if left_child_idx < last and nums[left_child_idx] > nums[largest_idx]:
                largest_idx = left_child_idx

            # Check if right child exists and is larger than the largest so far
            if right_child_idx < last and nums[right_child_idx] > nums[largest_idx]:
                largest_idx = right_child_idx

            # If the larger is not the current item, swap it with the largest child
            if largest_idx != curr:
                nums[curr], nums[largest_idx] = nums[largest_idx], nums[curr]
                # Recursively shift down from the largest index
                shift_down(largest_idx, nums, last)
            return

        build_heap(nums)
        for last in range(len(nums) - 1, 0, -1):
            nums[0], nums[last] = nums[last], nums[0]
            shift_down(0, nums, last)
        return nums

# nums = [5,2,3,1]
# print(Solution().sortArray(nums))
