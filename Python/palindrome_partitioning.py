class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def is_palindrome(s):
            return s == s[::-1]

        valid_partitionings = []

        def backtrack(start, end, partition):
            if end >= n:
                return
            curr = s[start:end + 1]

            if is_palindrome(curr):
                partition_copy = partition.copy()
                partition_copy.append(curr)
                if end == n - 1:
                    valid_partitionings.append(partition_copy)
                    return
                backtrack(end + 1, end + 1, partition_copy)

            backtrack(start, end + 1, partition)

        backtrack(0, 0, [])
        return valid_partitionings

