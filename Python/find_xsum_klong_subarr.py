import heapq


class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        n = len(nums)
        window = {}
        for i in range(k):
            num = nums[i]
            window[num] = window.get(num, 0) + 1

        ans = []
        for i in range(n - k + 1):
            max_heap = []
            for key, val in window.items():
                heapq.heappush(max_heap, (-val, -key))

            curr = 0
            for j in range(x):
                val, key = heapq.heappop(max_heap)
                curr += - val * -key
                if not max_heap:
                    break
            ans.append(curr)
            window[nums[i]] -= 1
            if i + k < n:
                window[nums[i + k]] = window.get(nums[i + k], 0) + 1
        return ans

