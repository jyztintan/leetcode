class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2 = m - 1, n - 1
        arr_ptr = m + n - 1
        for i in range(m + n - 1, -1, -1):
            if ptr1 < 0:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
                continue
            elif ptr2 < 0:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
                continue

            if nums1[ptr1] > nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 -= 1
        return nums1


nums1 = [4,5,6,0,0,0]
nums2 = [1,2,3]
print(Solution().merge(nums1, 3, nums2, 3))

