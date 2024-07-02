class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Keeps track of characters in nums1
        numbers = set()
        for num in nums1:
            numbers.add(num)
        ans = []
        for num in nums2:
            if num in numbers:
                ans.append(num)
                numbers.remove(num)
        return ans

# nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# print(Solution().intersection(nums1, nums2))
