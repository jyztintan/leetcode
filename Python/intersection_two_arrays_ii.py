class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Keeps track of numbers in nums1 array
        d = {}
        for num in nums1:
            # Increment each character count by 1
            d[num] = d.get(num, 0) + 1
        ans = []
        for num in nums2:
            # If the character is present in nums1 and if the character still hasn't reached its quota, then it is a valid intersect
            if num in d and d[num]:
                ans.append(num)
                # Used up 1 quota
                d[num] -= 1
        return ans

# nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# print(Solution().intersect(nums1, nums2))
