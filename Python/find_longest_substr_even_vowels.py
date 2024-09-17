class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}
        curr = 0
        seen = {0: -1}
        best = 0
        for i, c in enumerate(s):
            if c in vowels:
                curr = curr ^ vowels[c]
            if curr in seen:
                best = max(best, i - seen[curr])
            else:
                seen[curr] = i
        return best


print(Solution().findTheLongestSubstring("leetcodeisgreat"))
