class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        ptr = 0
        for idx, num in enumerate(nums):
            if num != val:
                count += 1
                nums[ptr] = num
                ptr += 1
        return count
