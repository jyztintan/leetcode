class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)
        sum1, sum2 = sum(nums1) + zeros1, sum(nums2) + zeros2

        if sum1 > sum2:
            return sum1 if zeros2 > 0 else -1
        elif sum2 > sum1:
            return sum2 if zeros1 > 0 else -1
        return sum1
