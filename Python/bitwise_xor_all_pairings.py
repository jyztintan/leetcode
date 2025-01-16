class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1, xor2 = 0, 0

        if len(nums2) % 2:
            for num in nums1:
                xor1 ^= num

        if len(nums1) % 2:
            for num in nums2:
                xor2 ^= num

        return xor1 ^ xor2
