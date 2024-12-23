# Time: O(N), Space: O(1) since we only use 2 pointers and don't need O(N) auxiliary space
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        left, right = 1, 1
        count = 1

        while right < len(nums):
            if nums[right] == nums[right - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[left] = nums[right]
                left += 1

            right += 1

        return left

# Time: O(N), Space: O(N)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        ptr = 0
        for idx, num in enumerate(nums):
            if num not in seen or seen[num] < 2:
                nums[ptr] = num
                ptr += 1
                seen[num] += 1
        for _ in range(ptr, len(nums)):
            nums.pop()
        return ptr