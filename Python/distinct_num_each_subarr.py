class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        # Set up initial window
        freq = {}
        for right in range(k):
            num = nums[right]
            freq[num] = freq.get(num, 0) + 1

        ans = [len(freq)]
        for right in range(k, len(nums)):
            num_right = nums[right]
            freq[num_right] = freq.get(num_right, 0) + 1
            left = right - k
            num_left = nums[left]
            freq[num_left] -= 1
            if freq[num_left] == 0:
                del freq[num_left]
            ans.append(len(freq))

        return ans
