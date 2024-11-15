import math


class Solution:
    def minimizedMaximum(self, n: int, quantities) -> int:

        # Number of product types
        total = sum(quantities)

        # Try different allocations of stores
        def distribute(k):
            print(list(math.ceil(q / k) for q in quantities))
            return sum(math.ceil(q / k) for q in quantities) <= n

        # The number of products distributed is [0, total quantity]
        low = 0
        high = total
        best = 0
        while low <= high:
            mid = (low + high)//2
            if distribute(mid):
                high = mid - 1
                best = mid
            else:
                low = mid + 1

        return best

