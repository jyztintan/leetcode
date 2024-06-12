class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_freq = {}
        for num in nums:
            num_freq[num] = 1 + num_freq.get(num, 0)
        lst = [[] for i in range(len(nums) + 1)]
        for key, value in num_freq.items():
            lst[value].append(key)
        ans = []
        for i in range(len(lst) - 1, 0, -1):
            ans.extend(lst[i])
            if len(ans) >= k:
                return ans

# sol = Solution()
# nums = [1,1,1,2,2,3]
# print(sol.topKFrequent(nums, 2))
