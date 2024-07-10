class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start = 0
        end = len(s) - 1
        while True:
            if start >= end:
                break
            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True

    def partition(self, s: str):

        ans = []

        def backtrack(idx, current_partition):
            if idx == len(s):
                ans.append(current_partition[:])
                return

            for end in range(idx + 1, len(s) + 1):
                substring = s[idx:end]
                if self.isPalindrome(substring):
                    current_partition.append(substring)
                    backtrack(end, current_partition)
                    current_partition.pop()

        backtrack(0, [])
        return ans
