class Solution:
    def minHeightShelves(self, books, shelfWidth: int) -> int:
        n = len(books)
        # This cache represents the minimum height for total shelf heights for books[i:]
        dp = [float('inf')] * n
        def dfs(i):
            # Out of bounds so just ignore
            if i >= n:
                return 0
            # If we computed before, then return the cached answer
            if dp[i] != float('inf'):
                return dp[i]
            # This helper function assumes that we are starting a new shelf with the book at index i
            curr_width = 0
            curr_height = 0
            # We attempt to put the remaining books in the shelf
            for j in range(i, n):
                width, height = books[j]
                # If putting the next book exceeds the shelf's width, then we stop
                if curr_width + width > shelfWidth:
                    break
                else:
                    # We add the next book to the shelf and modify the height
                    curr_width += width
                    curr_height = max(curr_height, height)
                    # For the subsequent book, we try making a new shelf to see if we potentially get a better answer
                    dp[i] = min(dp[i], dfs(j + 1) + curr_height)
            return dp[i]

        dfs(0)
        return dp[0]

# books = [[9,9],[5,4],[3,1],[1,5],[7,3]]
# print(Solution().minHeightShelves(books, 10))
