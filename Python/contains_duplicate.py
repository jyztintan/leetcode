class Solution(object):
    def containsDuplicate(self, nums):
        s = set()
        for ele in nums:
            if ele in s:
                return True
            s.add(ele)
        return False

