class Solution:
    def largestNumber(self, nums) -> str:
        if all(num == 0 for num in nums):
            return '0'
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x * 10, reverse=True)
        return "".join(nums)


nums = [3,30,34,5,9]
print(Solution().largestNumber(nums))

