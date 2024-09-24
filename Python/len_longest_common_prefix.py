class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        possible = set()
        for num in arr1:
            for i in range(len(num)):
                possible.add(num[:i + 1])
        longest = 0
        for num in arr2:
            for i in range(len(num)):
                if num[:i + 1] in possible:
                    longest = max(longest, len(num) - i)
        return longest


print(Solution().longestCommonPrefix([1, 10,100], [1000]))
