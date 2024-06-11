"""
167. Two Sum II - Input Array Is Sorted

- The tests are generated such that there is exactly one solution.
- You may not use the same element twice.
- Your solution must use only constant extra space.
"""

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1
        while True:
            total = numbers[start] + numbers[end]
            if total == target:
                return [start + 1, end + 1]
            elif total < target:
                start += 1
            else:
                end -= 1

# s = Solution()
# numbers =[2,7,11,15]
# print(s.twoSum(numbers, 13))