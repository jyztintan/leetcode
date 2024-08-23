class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        memoized = {}

        def count_dist(w1, w2):
            if w1 == w2:
                return 0

            if not w1:
                return len(w2)

            if not w2:
                return len(w1)

            if (w1, w2) in memoized:
                return memoized[(w1, w2)]

            if w1[0] == w2[0]:
                ans = count_dist(w1[1:], w2[1:])
            else:
                # inserting a character into w1 start is equivalent to deleting the first character in w2
                insert = count_dist(w1, w2[1:]) + 1

                # replacing is equivalent marking the first character of w1 as processed
                replace = count_dist(w1[1:], w2[1:]) + 1

                delete = count_dist(w1[1:], w2) + 1

                ans = min(insert, replace, delete)

            memoized[(w1, w2)] = ans
            return ans

        return count_dist(word1, word2)

# print(Solution().minDistance("a", "b"))

