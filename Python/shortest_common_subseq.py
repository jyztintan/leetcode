

# Time: O(N * M * (N + M)), Space: O(N * M * (N + M)) due to string concatenation O(N + M) within each subproblem
# As a result, this approach exceeds memory limit :(
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memoize = {}

        def find_shortest(ptr1, ptr2):
            if (ptr1, ptr2) in memoize:
                return memoize[(ptr1, ptr2)]
            if ptr1 < 0:
                return str2[:ptr2 + 1]
            if ptr2 < 0:
                return str1[:ptr1 + 1]

            if str1[ptr1] == str2[ptr2]:
                return find_shortest(ptr1 - 1, ptr2 - 1) + str1[ptr1]

            attempt1 = find_shortest(ptr1 - 1, ptr2) + str1[ptr1]
            attempt2 = find_shortest(ptr1, ptr2 - 1) + str2[ptr2]

            if len(attempt1) < len(attempt2):
                memoize[(ptr1, ptr2)] = attempt1
            else:
                memoize[(ptr1, ptr2)] = attempt2
            return memoize[(ptr1, ptr2)]

        return find_shortest(len(str1) - 1, len(str2) - 1)
