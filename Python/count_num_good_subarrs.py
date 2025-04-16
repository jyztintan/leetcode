class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = {}
        curr = 0
        count = 0
        n = len(nums)
        right = 0
        for left, num in enumerate(nums):
            while curr < k and right < n:
                add_num = nums[right]
                curr += freq.get(add_num, 0)
                freq[add_num] = freq.get(add_num, 0) + 1
                right += 1

            if curr >= k:
                count += n - right + 1

            freq[num] -= 1
            curr -= freq[num]
        return count

