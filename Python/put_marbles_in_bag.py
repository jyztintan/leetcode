# Approach 1: Sort and get!
# Time Complexity: O(NlogN) for sorting
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        checkpoints = []
        n = len(weights)
        for ptr in range(n - 1):
            checkpoints.append(weights[ptr] + weights[ptr + 1])

        checkpoints.sort()
        min_score = sum(checkpoints[:k - 1])
        max_score = sum(checkpoints[-(k - 1):])
        return max_score - min_score

# Approach 2: Heapify and extracting top k
# Time Complexity: O(N + klogN)
import heapq
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        max_checkpoints = []
        min_checkpoints = []
        n = len(weights)
        for ptr in range(n - 1):
            max_checkpoints.append(- weights[ptr] - weights[ptr + 1])
            min_checkpoints.append(weights[ptr] + weights[ptr + 1])

        heapq.heapify(max_checkpoints)
        heapq.heapify(min_checkpoints)
        max_score, min_score = 0, 0
        for _ in range(k - 1):
            max_score -= heapq.heappop(max_checkpoints)
            min_score += heapq.heappop(min_checkpoints)
        return max_score - min_score

# Approach 3: Quick Select
# Time Complexity: O(N)
def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quickselect(arr, k):
    left, right = 0, len(arr) - 1
    while left <= right:
        pivot_index = partition(arr, left, right)
        if pivot_index == k:
            return
        elif pivot_index < k:
            left = pivot_index + 1
        else:
            right = pivot_index - 1

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        checkpoints = []
        n = len(weights)
        for ptr in range(n - 1):
            checkpoints.append(weights[ptr] + weights[ptr + 1])

        max_checkpoints = checkpoints[:]
        quickselect(max_checkpoints, n - k)
        max_score = sum(max_checkpoints[n - k:])

        min_checkpoints = checkpoints[:]
        quickselect(min_checkpoints, k - 1)
        min_score = sum(min_checkpoints[:k - 1])

        return max_score - min_score
