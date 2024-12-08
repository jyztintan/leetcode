class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        low, high = 1, max(ribbons)
        def can_cut(x):
            groups = [ribbon // x for ribbon in ribbons]
            return sum(groups) >= k

        best = 0
        while low <= high:
            mid = (low + high) // 2
            # Can cut k groups of length x, so we try to increase x and see if still can cut
            if can_cut(mid):
                best = max(best, mid)
                low = mid + 1
            # Can't cut k groups of length x, so we reduce x and see if we can cut k groups
            else:
                high = mid - 1
        return best
