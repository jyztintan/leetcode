class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0] * (length + 1)
        for start, end, incr in updates:
            nums[start] += incr
            nums[end + 1] += -incr

        for i in range(1, length):
            nums[i] += nums[i - 1]
        return nums[:-1]
