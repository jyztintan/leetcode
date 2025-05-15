class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        prev = -1
        for i in range(len(groups)):
            if groups[i] != prev:
                ans.append(words[i])
                prev = groups[i]
        return ans
