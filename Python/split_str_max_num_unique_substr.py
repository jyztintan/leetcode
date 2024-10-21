class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)

        def find_unique(seen, left):
            if left == n:
                return 0

            count = 0
            for right in range(left + 1, n + 1):
                substr = s[left:right]
                if substr not in seen:
                    seen.add(substr)
                    count = max(count, find_unique(seen, right) + 1)
                    seen.remove(substr)
            return count

        return find_unique(set(), 0)


# print(Solution().maxUniqueSplit(""))
