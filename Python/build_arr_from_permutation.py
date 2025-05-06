# Time: O(N), Space: O(1) since we modify in place
# We "encode" the processed elements as the remainder of % n
# This works as the array is zero-based permutation,
# that is for all num in nums: 0 <= num < n
# Hence the "decryption" process will not break when unpacking the processed array
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i, num in enumerate(nums):
            nums[i] += n * (nums[num] % n)

        return list(map(lambda x: x // n, nums))

# Time: O(N), Space: O(N)
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(nums[num])
        return ans