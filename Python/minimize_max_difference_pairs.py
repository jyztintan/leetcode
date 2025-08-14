class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        low, high = 0, nums[-1] - nums[0]
        while low < high:  # always
            mid = (low + high) // 2
            # try to find p pairs with difference of `mid`
            count = 0
            ptr = 0
            while ptr < n - 1:
                if nums[ptr + 1] - nums[ptr] <= mid:
                    ptr += 1
                    count += 1
                ptr += 1
            if count >= p:
                # we can try to lower the difference
                high = mid
            else:
                # cannot form so need to increase difference
                low = mid + 1
        return low
        # see if we can form p pairs within this difference
