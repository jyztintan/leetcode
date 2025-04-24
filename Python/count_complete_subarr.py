class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        n = len(nums)
        right = 0

        count = 0
        window = {}
        for left in range(n):
            while right < n and len(window) < target:
                num = nums[right]
                window[num] = window.get(num, 0) + 1
                right += 1
            if len(window) == target:
                count += n - right + 1

            remove = nums[left]
            window[remove] -= 1
            if window[remove] == 0:
                del window[remove]

        return count
