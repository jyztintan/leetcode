import heapq
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n - k + 1):
            window = nums[i: i + k]
            counter = Counter(window)
            kv = counter.items()
            kv = sorted(list(kv), key=lambda x:(x[1], x[0]))
            x_sum = sum(t[0] * t[1] for t in kv[-x:])
            ans.append(x_sum)
        return ans

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

