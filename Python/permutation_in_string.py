class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If there are more letters in s1 than s2, impossible for s2 to have a permutation substring s1
        if len(s1) > len(s2):
            return False

        # Keep track of letters we are accounting for
        target = [0] * 26
        window = [0] * 26

        # Increment the relevant letter buckets of s1
        for c in s1:
            target[ord(c) - ord('a')] += 1

        # The first window is the first len(s1) letters in s2
        n = len(s1)
        for i in range(n):
            window[ord(s2[i]) - ord('a')] += 1

        # We incrementally slide the window while there is no matching list
        left = 0
        for right in range(n, len(s2)):
            if window == target:
                return True
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1
            window[ord(s2[right]) - ord('a')] += 1

        return window == target



# print(Solution().checkInclusion("ab","eidbaooo"))
# print(Solution().checkInclusion("ab","eidboaoo"))
# print(Solution().checkInclusion("mart","karma"))
