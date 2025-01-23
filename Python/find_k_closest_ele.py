class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        # We find the leftmost starting index
        while left < right:
            mid = (left + right) // 2
            # Within the subarray, the gap with the leftmost element must be smaller than the gap with the rightmost element
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]
