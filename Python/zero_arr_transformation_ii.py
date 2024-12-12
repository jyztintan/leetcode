from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        def create_decr(k):
            decr = [0] * (n + 1)
            for left, right, val in queries[:k]:
                decr[left] -= val
                decr[right + 1] += val
            return decr

        def is_zero_arr(decr):
            curr = 0
            for idx in range(n):
                curr += decr[idx]
                if nums[idx] + curr > 0:
                    return False
            return True

        ans = float('inf')
        low, high = 0, len(queries)
        while low <= high:
            mid = (low + high) // 2
            decr = create_decr(mid)
            if is_zero_arr(decr):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        if ans == float('inf'):
            return -1
        return ans


nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
print(Solution().minZeroArray(nums, queries))