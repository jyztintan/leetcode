class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # If total letters dont add up then straight away reject
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[None] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def dfs(ptr1, ptr2):
            # Both pointers of s1 and s2 reached the end; We managed to somehow interleave s1 and s2 to form s3!
            if ptr1 == len(s1) and ptr2 == len(s2):
                return True

            # If we have seen this before, just output the already computed solution
            if dp[ptr1][ptr2] is not None:
                return dp[ptr1][ptr2]

            # Check if we can use the current letter at the pointer of s1 to make up s3
            if ptr1 < len(s1) and s1[ptr1] == s3[ptr1 + ptr2]:
                if dfs(ptr1 + 1, ptr2):
                    dp[ptr1][ptr2] = True
                    return True

            # Check if we can use the current letter at the pointer of s2 to make up s3
            if ptr2 < len(s2) and s2[ptr2] == s3[ptr1 + ptr2]:
                if dfs(ptr1, ptr2 + 1):
                    dp[ptr1][ptr2] = True
                    return True

            # If we cannot use either means impossible to form s3 through this interleaving
            dp[ptr1][ptr2] = False
            return False

        return dfs(0,0)

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# print(Solution().isInterleave(s1, s2, s3))
