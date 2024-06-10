class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0

        # modulos
        d = {}
        current_mod = 0
        for num in nums:
            current_mod += num
            current_mod = current_mod % k
            if current_mod not in d:
                if current_mod == 0:
                    d[current_mod] = 1
                else:
                    d[current_mod] = 0
            ans += d[current_mod]
            d[current_mod] += 1
        return ans

# Testing
sol = Solution()
nums = [4,5,0,-2,-3,1]
print(sol.subarraysDivByK(nums, 5))