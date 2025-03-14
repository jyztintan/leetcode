class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)
        if total < k:
            return 0

        low, high = 1, total // k
        best = 0
        while low <= high:
            mid = (low + high) // 2
            # Check if possible to distribute
            children = sum(pile // mid for pile in candies)
            if children >= k:
                best = mid
                low = mid + 1
            else:
                high = mid - 1
        return best

