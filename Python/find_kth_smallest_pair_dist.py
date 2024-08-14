class Solution:
    # There will be (n * (n - 1))/2 pairs to compare
    def smallestDistancePair(self, nums, k: int) -> int:
        nums.sort()
        def count_pairs(max_diff):
            count = left = 0
            for right in range(len(nums)):
                while nums[right] - nums[left] > max_diff:
                    left += 1
                count += (right - left)
            return count


        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high)//2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

nums = [1,3,1]
print(Solution().smallestDistancePair(nums, 1))

