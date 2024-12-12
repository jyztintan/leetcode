# O(N) pass
# O(N) space
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        decr = [0] * (n + 1)
        for left, right in queries:
            decr[left] -= 1
            decr[right + 1] += 1

        curr = 0
        for idx in range(n):
            curr += decr[idx]
            if nums[idx] + curr > 0:
                return False
        return True


# O(NlogN) for sorting (after creating events)
# O(N) space
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        events = []
        for left, right in queries:
            events.append((left, -1))
            events.append((right + 1, 1))

        events.sort()
        curr_decr = 0
        ptr = 0
        for idx in range(len(nums)):
            while events[ptr][0] <= idx:
                curr_decr += events[ptr][1]
                ptr += 1

            if nums[idx] + curr_decr > 0:
                return False
        return True
