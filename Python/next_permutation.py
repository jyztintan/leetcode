class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # Find first instance of decreasing digits from right to left
        left = n - 2
        while left >= 0 and nums[left + 1] <= nums[left]:
            left -= 1

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Edge case: digits are already descending (last permutation) so we return them ascending (first permutaion)
        if left == -1:
            reverse(0, n - 1)
            return nums

        # Find the digit that is greater than left and swap
        right = n - 1
        while nums[right] <= nums[left]:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]

        # After swapping, we reverse the remaining to get the next lexicographical permutation
        reverse(left + 1, n - 1)
        return nums
