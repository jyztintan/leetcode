class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        k_distant = []
        right = 0
        for curr, num in enumerate(nums):
            if num == key:
                left = max(right, curr - k)
                right = min(len(nums) - 1, curr + k) + 1
                for i in range(left, right):
                    k_distant.append(i)
        return k_distant
