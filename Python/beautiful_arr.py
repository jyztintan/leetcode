class Solution:
    def beautifulArray(self, n: int):
        memoize = {1:[1]}

        def helper(n):
            if n in memoize:
                return memoize[n]

            # We construct the beautiful subarray recursively by always separating odds and evens
            odds = helper(n // 2 + n % 2)
            odds = list(map(lambda x : 2 * x - 1, odds))
            even = helper(n // 2)
            even = list(map(lambda x : 2 * x, even))

            memoize[n] = odds + even
            return memoize[n]

        return helper(n)
