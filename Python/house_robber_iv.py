class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low, high = min(nums), max(nums)
        n = len(nums)

        while low < high:
            mid = (low + high) // 2
            house = 0
            ptr = 0
            while ptr < n:
                if nums[ptr] <= mid:
                    house += 1
                    ptr += 2
                else:
                    ptr += 1

            if house >= k:
                high = mid
            else:
                low = mid + 1
        return low
