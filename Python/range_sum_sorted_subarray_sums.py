from typing import List

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        subarray_sums = []
        prev = []
        for num in nums:
            to_add = [num]
            for sub_sum in prev:
                to_add.append(sub_sum + num)
            subarray_sums.extend(to_add)
            prev = to_add

        subarray_sums.sort()
        return sum(subarray_sums[left - 1:right]) % (10**9 + 7)

# print(Solution().rangeSum([1,2,3,4], 4, 1, 5))
