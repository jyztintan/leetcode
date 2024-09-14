class Solution:
    def longestSubarray(self, nums) -> int:
        ptr = 0
        highest = -1
        ans = 0
        while ptr < len(nums):
            if nums[ptr] > highest:
                count = 1
                highest = nums[ptr]
                while ptr + 1 < len(nums) and nums[ptr + 1] == highest:
                    count += 1
                    ptr += 1
                ans = count
                ptr += 1
            elif nums[ptr] == highest:
                count = 1
                while ptr + 1 < len(nums) and nums[ptr + 1] == highest:
                    count += 1
                    ptr += 1
                ans = max(ans, count)
                ptr += 1
            else:
                ptr += 1
        return ans

# class Solution:
#     def longestSubarray(self, nums) -> int:
#         highest = max(nums)
#         longest = 0
#         count = 0
#         for num in nums:
#             if num == highest:
#                 count += 1
#             else:
#                 longest = max(longest, count)
#                 count = 0
#         longest = max(longest, count)
#         return longest


nums = [96317,96317,96317,96317,96317,96317,96317,96317,96317,279979]
print(Solution().longestSubarray(nums))
nums = [1,2,3,4]
print(Solution().longestSubarray(nums))
nums = [10,2,2,2,3,3,5,5]
print(Solution().longestSubarray(nums))
