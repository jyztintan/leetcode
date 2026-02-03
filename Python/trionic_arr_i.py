class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ptr = 0
        n = len(nums)

        def move(condition):
            nonlocal ptr
            before = ptr
            while ptr + 1 < n and condition(nums[ptr], nums[ptr + 1]):
                ptr += 1
            return ptr > before

        return move(lambda x, y: y > x) and move(lambda x, y: x > y) and move(lambda x, y: y > x) and ptr == n - 1


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        ptr = 0
        n = len(nums)
        before = ptr
        while ptr + 1 < n and nums[ptr + 1] > nums[ptr]:
            ptr += 1
        if before == ptr:
            return False

        before = ptr
        while ptr + 1 < n and nums[ptr + 1] < nums[ptr]:
            ptr += 1
        if before == ptr:
            return False

        before = ptr
        while ptr + 1 < n and nums[ptr + 1] > nums[ptr]:
            ptr += 1
        if before == ptr:
            return False
        return ptr == n - 1
