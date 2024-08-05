class Solution:
    def kthDistinct(self, arr, k: int) -> str:

        strings = {}
        for i, s in enumerate(arr):
            if s in strings:
               strings[s] = False
            else:
                strings[s] = True

        count = 0
        for key in strings:
            if strings[key]:
                count += 1
                if count == k:
                    return key
        return ""

# arr = ["a", "b", "a", "c", "d", "b", "e"]
# print(Solution().kthDistinct(arr, 2))