class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def can_fit(k):

            # Keep track num of operations
            count = 0

            for num in nums:
                if num <= k:
                    continue
                # Note that it is in its negative form
                split_piles = ceil(num / k)
                count += split_piles - 1
            return count <= maxOperations

        low, high = 1, max(nums)
        best = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if can_fit(mid):
                best = mid
                high = mid - 1
            else:
                low = mid + 1
        return best
