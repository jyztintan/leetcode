class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ptr2 = 0
        dist = 0
        for ptr1, num in enumerate(nums1):
            while ptr2 + 1 < len(nums2) and nums2[ptr2 + 1] >= num:
                ptr2 += 1
            dist = max(dist, ptr2 - ptr1)
        return dist
