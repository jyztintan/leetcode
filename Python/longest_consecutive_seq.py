# This time complexity seems like it is O(N^2) but is actually O(N) because we only process the while loop
# for numbers which are the start of the streak.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 in nums:
                continue
            count = 1
            while num + 1 in nums:
                count += 1
                num += 1
            longest = max(longest, count)
        return longest

# s = Solution()
# nums = [100,4,200,1,3,2]
# print(s.longestConsecutive(nums))

# nums = [0,3,7,2,5,8,4,6,0,1]
# print(s.longestConsecutive(nums))
