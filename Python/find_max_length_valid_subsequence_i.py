class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        nums = [num % 2 for num in nums]
        even, odd = 0, 0
        even_alt = odd_alt = 0
        for num in nums:
            if num % 2:
                odd += 1
                even_alt = odd_alt + 1
            else:
                even += 1
                odd_alt = even_alt + 1
        return max(even_alt, odd_alt, even, odd)
