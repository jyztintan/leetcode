class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = min(len(word1), len(word2))
        ans = ""
        for i in range(n):
            ans += word1[i]
            ans += word2[i]

        if len(word1) > n:
            ans += word1[n:]
        elif len(word2) > n:
            ans += word2[n:]
        return ans

