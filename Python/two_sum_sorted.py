"""
- The tests are generated such that there is exactly one solution.
- You may not use the same element twice.
- Your solution must use only constant extra space. This implementation is more optimised than the hash set
algorithm used in the classic Two Sum since we don't need additional O(N) space.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers) - 1
        while left_ptr < right_ptr:
            curr_sum = numbers[left_ptr] + numbers[right_ptr]
            if curr_sum == target:
                return [left_ptr + 1, right_ptr + 1]
            elif curr_sum > target:
                right_ptr -= 1
            else:
                left_ptr += 1

# s = Solution()
# numbers =[2,7,11,15]
# print(s.twoSum(numbers, 13))
